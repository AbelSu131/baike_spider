# coding=utf-8
class HtmlOutputer(object):
    #初始化
    def __init__(self):
        self.datas = []

    def collect_data(self, data):   #收集数据
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):  #输出数据
        fout = open('output.html', 'w')

        fout.write("<html>")

        fout.write("<head>")
        fout.write("<meta charset= 'UTF-8'>")
        fout.write("</head>")

        fout.write("<body>")
        fout.write("<table>")

        # ASCII
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</html>")
        fout.write("</body>")
        fout.write("</table>")

        fout.close()