from tornado.web import RequestHandler
from tornado import gen
import asyncio
import tornado.ioloop


class IndexHandler(RequestHandler):
    def get(self):
        self.write('this is index')


class BlockingHandler(RequestHandler):
    async def get(self):
        import time
        print(time.time())
        task_list = [self.dosomething() for i in range(2)]
        # 多个无关的异步任务实现并发
        body = await asyncio.wait(task_list)

        for i in body[0]:
            # 返回的task是无序的  result()是返回值
            print(i.result())

        # result1 = await self.dosomething()
        # result2 = await self.dosomething()
        # self.write(result1 + result2)
        print(time.time())

    async def dosomething(self):
        # 如果是其他处理函数或者逻辑，要保证函数是协程
        await gen.sleep(2)
        print("wait 2 s")
        return 'block end'


app = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/blocking", BlockingHandler)
])
if __name__ == "__main__":
    app.listen(8001)
    tornado.ioloop.IOLoop.instance().start()