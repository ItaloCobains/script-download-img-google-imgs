import requests
from bs4 import BeautifulSoup

run = True

pasta = str(input("qual o caminho da pasta: "))

while run:
    search = str(input("Qual imagem vc quer baixar ?  "))
    num_of_img = int(input("Numero de imagens que vc deseja baixar: "))
    print('')
    print("Downloading........")
    print('')

    links_list = []
    img_list = []
    img_index = 0
    page_number = (num_of_img//20)*20
    url1 = f'https://www.google.com/search?q={search}+4k&client=opera-gx&gbv=1&sxsrf=AOaemvKJu__Olf2DnFm_oH6nAfgFk4OBKQ:1635179145955&source=lnms&tbm=isch&sa=X&ved=2ahUKEwja1I2B_eXzAhVKGLkGHaQWB-cQ_AUoAXoECAEQAw&biw=1325&bih=658&dpr=1&sfr=gws&sei=rtp2YcuHOf7o5OUPs-SGwAs'
    req = requests.get(url1)
    soup = BeautifulSoup(req.text, 'html.parser')

    for img in soup.findAll('img')[1:]:
        if img_index == num_of_img:
            break
        else:
            links_list.append(img.get('src'))
            img_index += 1

    for links  in links_list:
        img_list.append(requests.get(links))

    for i,img in enumerate(img_list):
        with open(f'{pasta}/{search}_{i}.png', 'wb') as f:
            f.write(img.content)

    for pages in range(20, page_number + 20, 20):
        img_list = []
        links_list = []

        if(img_index == num_of_img):
            break
        else:
            urln = f'https://www.google.com/search?q={search}+4k&client=opera-gx&gbv=1&biw=1325&bih=658&tbm=isch&sxsrf=AOaemvJd9owU8aasekzZUnLzEbuu3aTLXg:1635179183716&ei=r9p2Yf2JK8zZ1sQP19-A8AQ&start={pages}&sa=N'
            req = requests.get(urln)
            soup = BeautifulSoup(req.text, 'html.parser')

            for img in soup.findAll('img')[1:]:
                if img_index == num_of_img:
                    break
                else:
                    links_list.append(img.get('src'))
                    img_index += 1
            for links in links_list:
                img_list.append(requests.get(links))

            for i, img in enumerate(img_list):
                with open(f'{pasta}/{search}_{i + img_index - len(links_list)}.png', 'wb') as f:
                    f.write(img.content)
    print("!DONE")
    if img_index < num_of_img:
        print(f"It was no possible to download {img_index} images")
        print('')
    if img_index == 0:
        print("Unfortunately we did not find any image to download")
        print('')
    exit_question = str(input("Quer sair ? [Y/N]"))
    if exit_question.upper()[0] == 'Y':
        break
    else:
        continue
print('')
print(50*'-')
print("https://github.com/ItaloCobains")
