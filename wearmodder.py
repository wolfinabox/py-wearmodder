import os,sys
COEFFICIENT=2

def processRange(content:str,units:str,min:int,max:int):
    for i in range(min,max):
        content=content.replace(">" + str(i) + ".0" + units, ">" + str(i//COEFFICIENT) + ".0" + units).replace("\"" + str(i) + ".0" + units, "\"" + str(i//COEFFICIENT) + ".0" + units)
    return content


def processFile(path:str):
    if os.path.splitext(path)[1]!='.xml':
        return;
    print(path)
    try:
        with open(path,'r') as f:
            try:
                text=''.join(f.readlines())
            except UnicodeDecodeError:
                return
        text = processRange(text, "dip", 2, 720);
        text = processRange(text, "sp", 2, 240);
        text=text.replace(">?android:actionBarSize<", ">28.0dip<").replace("\"?actionBarSize\"", "\"28.0dip\"")
        with open(path,'w') as f:
            f.write(text)
        

    except IOError as e:
        print(e)



if len(sys.argv)<2:
    print('Run this script passing the path to the app\'s "res" folder as the argument.')
    exit()

path=sys.argv[1]

if not os.path.isdir(path):
    print(f'Path "{path}" either does not exist, or is not a dir')
    exit()

for root,dirs,files in os.walk(path):
    for name in files:
        processFile(os.path.join(root,name))