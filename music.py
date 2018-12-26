
#导入歌手的信息类
import songer_id_parse
#导入歌曲的评论解析类
import song_discuss_parse
#导入歌曲的中间函数，作用为爬取歌手歌曲的id
import song_middle

import json

def songer_id():
    songer = songer_id_parse.Encrypyed()
    songer_id = songer.parse(0, 60)
    text=json.loads(songer_id.text)
    return text['artists']
def song_discuss(song_id):
    song=song_discuss_parse.Encrypyed()
    text=song.parse(song_id,1,80)#第一个参数为歌曲id，第二个为偏移量，表示和第一个的距离，第三个为显示的个数
    comment=json.loads(text.text)

    #这个parse函数，在偏移量为0时，数据在artists，之后再comments
    return comment['comments']
    # for i in comment['comments']:
    #     print(i['user']['nickname'])

def disk_file():
    # 1首先获取歌手的id
    info = {}
    data = songer_id()
    for inf in data:
        # inf['name']  歌手名字
        print('正在存'+inf['name']+'的歌曲评论')
        filename=inf['name']+'.txt'
        f=open(filename,'w',encoding='utf-8')
        song_id=song_middle.parse_song_id(inf['id'])
        #返回歌手歌曲id
        for song in song_id:
            #解析歌曲的评论
            print('正在写'+song_id[song]+'的评论')
            f.write('《'+song_id[song]+'》'+'\n'+song+'\n\n')
            #先写入歌曲名称和id换行
            comment=song_discuss(song)
            count=1
            for comm in comment:
               f.write('第'+str(count)+'条： '+comm['user']['nickname']+' : '+comm['content']+'\n')
               info[comm['user']['nickname']]=comm['content']
               count+=1
            print('写' + song_id[song] + '的评论完毕')
        f.close()
        print(inf['name']+'存取完毕')

if __name__=='__main__':
    #将文件存储在本地
    disk_file()



