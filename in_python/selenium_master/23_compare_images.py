import cv2


def compare_images(image1, image2):
    flag = False

    image1 = cv2.imread(image1)
    image2 = cv2.imread(image2)

    rows1, cols1, channel1 = image1.shape
    rows2, cols2, channel2 = image2.shape

    if (rows1, cols1, channel1) != (rows2, cols2, channel2):
        return flag
    else:
        cntr = 0
        for i in range(1, rows1):
            for j in range(1, cols1):
                px1 = image1[i, j]
                px2 = image2[i, j]

                if px1.sum() != px2.sum():
                    cntr += 1

        if not cntr:
            flag = True
            return flag
        else:
            return flag

print(compare_images(r'C:\Users\gsingh\Dropbox\Technical\Selenium\TheLearnSeleniumProject\selenium_master\files\v1.jpg',
               r'C:\Users\gsingh\Dropbox\Technical\Selenium\TheLearnSeleniumProject\selenium_master\files\v2.jpg'))

print(compare_images(r'C:\Users\gsingh\Dropbox\Technical\Selenium\TheLearnSeleniumProject\selenium_master\files\v1.jpg',
               r'C:\Users\gsingh\Dropbox\Technical\Selenium\TheLearnSeleniumProject\selenium_master\files\v3.jpg'))
