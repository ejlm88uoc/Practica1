import scrapy
import requests
import pandas as pd

class QuotesSpider(scrapy.Spider):
    name = "pec"
    start_urls = [
        'https://www.ascodevida.com/ultimos/p/1',
    ]

    def parse(self, response):
        data = pd.DataFrame(columns=('id', 'author', 'type', 'date', 'text', 'comment', 'queAdv', 'merecido', 'chorrada'))
        adv = response.css("div.box.story")
        for advTemp in adv:
            comment = advTemp.css("div.comment_tag span a.comments::text").get()
            textAdv = advTemp.css("p.story_content.storyTitle a.advlink::text").get()
            id = str(advTemp.css("div.comment_tag span a::attr(id)").get()).split("_")[1]
            votesTemp = advTemp.css("div.meta span::text").getall()
            queAdv = votesTemp[0].split("(")[1].split(")")[0]
            merecido = votesTemp[1].split("(")[1].split(")")[0]
            chorrada = votesTemp[2].split("(")[1].split(")")[0]
            temp = advTemp.css("div.pre a::attr(href)").getall()
            author = None
            typeAdv = None
            datePub = None
            temp2 = advTemp.css("div.pre a::text").getall()
            temp3 = advTemp.css("div.pre::text").getall()
            if 'https://www.ascodevida.com/usuarios' in temp[0]:
                author = temp2[0]
                typeAdv = temp2[1]
                datePub = temp3[2]
            else:
                author = temp3[1].split(" el ")[0]
                typeAdv = temp2[0]
                datePub = temp3[1].split(" el ")[1]
            datePub = datePub.split(" /")[0]
            addData = {'id': id, 'author': author, 'type': typeAdv, 'date':datePub, 'text': textAdv, 'comment': comment, 'queAdv': queAdv, 'merecido': merecido, 'chorrada': chorrada}
            data = data.append(addData, ignore_index=True)
        if response.url == 'https://www.ascodevida.com/ultimos/p/1':
            data.to_csv('advData.csv', index=False)
        else:
            df = pd.read_csv('advData.csv', index_col=0)
            df = df.append(data)
            df.to_csv('advData.csv', index=False)

        nextUrl = response.url.split("/p/")
        nextUrl = nextUrl[0] + "/p/" + str(int(nextUrl[1]) + 1)
        if  requests.get(nextUrl).status_code is 200:
            yield scrapy.Request(nextUrl, callback=self.parse)