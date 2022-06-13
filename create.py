from PIL import Image,ImageFont,ImageDraw


import random




def main(a,b,c,order,text,nextnaiyou,month,day,jikan,yokatta,mochi,shuku):
  image_path = './main.png'
  font_path = './corp.ttf'
  font_size = 32 #文字の大きさ
  #JST = datetime.timezone(datetime.timedelta(hours=+9), 'JST')

  # GOOD, タイムゾーンを指定している．早い
  
  #text = datetime.datetime.now(JST).isoformat(" ","seconds")
  #text=text.replace("+09:00","")
  #print(text)
  color = (0,0,0)#文字の色
  image = Image.open(image_path)
  font = ImageFont.truetype(font_path,font_size)#フォントの指定
  draw = ImageDraw.Draw(image)
  #main
  font = ImageFont.truetype(font_path,70)
  draw.text((950,270),f"{a}",font=font,fill=color)
  #-----
  font = ImageFont.truetype(font_path,70)
  draw.text((950,390),f"{b}",font=font,fill=color)
  font = ImageFont.truetype(font_path,70)
  draw.text((950,510),f"{c}",font=font,fill=color)
  font = ImageFont.truetype(font_path,50)
  draw.text((30,670),text,font=font,fill=color)
  
  font = ImageFont.truetype(font_path,50)
  draw.text((1100,680),nextnaiyou,font=font,fill=color)
  #month
  font = ImageFont.truetype(font_path,50)
  draw.text((260,60),month,font=font,fill=color)
  #day
  font = ImageFont.truetype(font_path,50)
  draw.text((540,60),day,font=font,fill=color)
  #jikan
  font = ImageFont.truetype(font_path,50)
  draw.text((820,60),jikan,font=font,fill=color)

  font = ImageFont.truetype(font_path,50)
  draw.text((1090,100),yokatta,font=font,fill=color)

  font = ImageFont.truetype(font_path,50)
  draw.text((1260,397),f"{mochi}",font=font,fill=color)

  font = ImageFont.truetype(font_path,50)
  draw.text((1260,515),f"{shuku}",font=font,fill=color)


  
  image.save(f"static/{order}.png")
  
 
if __name__ == '__main__':
  main("A","B","C",str(random.randint(100001,999998)),"ああああ"+'\n'+"ああああ","連立","5","15","5","どこかがよかった","ふでばこ","ノート")
