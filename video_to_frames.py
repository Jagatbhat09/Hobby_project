import cv2,csv,os,sys,shutil

def dump_to_csv(filename,list_to_dump_in_csv) :
    with open(filename , 'w') as f :
        wr = csv.writer(f)
        for k in list_to_dump_in_csv :
            wr.writerow(k)


def video_to_frame(filname,dirname) :
    vidcap = cv2.VideoCapture(filname)
    success,image = vidcap.read()
    count = 0
    success = True
    if os.path.exists(dirname) :
        shutil.rmtree(dirname)
    os.makedirs(dirname)
    while success :
        count += 1
        success,image = vidcap.read()
        print 'read a new frame',success
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        m,n = gray.shape
        gray_scale_csv = [[0 if gray[i,j] < 100  else 1 for j in range(n)] for i in range(m)]
        dirnam= dirname + "/frame_%d"%count+".csv"
        dump_to_csv(dirnam,gray_scale_csv)


def main()  :
	video_to_frame(sys.argv[1],sys.argv[1].split(".")[0])

main()

