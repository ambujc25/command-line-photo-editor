from PIL import Image
import sys

filename = input("Enter file name: ")
im = Image.open(filename)

print("1.Change format\n2.Resize\n3.Crop\n4.PasteImage\n5.Rotate\n6.Flip")

try:
	oper = int(input(""))
except:
	print("Not a valid operation")
	quit()

if oper == 1:
	print("Current format:", im.format)
	new_format = input("Change to: ")
	name = filename.split(".")
	
	try:
		im.save(name[0]+"."+new_format)
	except:
		print("Not a valid format")
		quit()

elif oper == 2:
	print("Current Size:", im.size)
	x = input("Enter size separated with a comma: ")
	x = x.split(',')

	new_image = im.resize((int(x[0]),int(x[1])))
	name = filename.split(".")
	new_image.save(name[0]+"_resized."+name[1])

elif oper==3:
	x = input("Enter crop coordinates(left,upper,right,lower) separated with a comma: ")
	x = x.split(',')

	box = (int(x[0]),int(x[1]),int(x[2]),int(x[3]))
	cropped = im.crop(box)

	name = filename.split(".")
	cropped.save(name[0]+"_cropped."+name[1])

elif oper==4:
	new_image = input("Enter name of image you want to paste: ")
	im_new = Image.open(new_image)

	original_copy = im.copy()
	pos = int(input("1.TopLeft\n2.TopRight\n3.BottomLeft\n4.BottomRight\n5.Center\n6.Custom\n"))
	
	if pos==1:
		position = (0,0)
	elif pos==2:
		position = (original_copy.width - im_new.width,0)
	elif pos==3:
		position = (0,original_copy.height - im_new.height)
	elif pos==4:
		position = (original_copy.width - im_new.width,original_copy.height - im_new.height)
	elif pos==5:
		position = (int((original_copy.width - im_new.width)/2),int((original_copy.height - im_new.height)/2))
	elif pos==6:
		x = input("Enter coordinates separated with a comma: ")
		x = x.split(',')
		position = (int(x[0]),int(x[1]))

	#If the image has an transparent background it has an alpha value as well, by passing the image again
	#as the third argument, it masks the background out leaving us with a transparent background
	try:
		original_copy.paste(im_new,position,im_new)
	except:
		original_copy.paste(im_new,position)

	name = filename.split(".")
	original_copy.save(name[0]+"_pasted."+name[1])

elif oper==5:
	amount = float(input("Enter degrees to rotate (counterclockwise): "))
	rotated_image = im.rotate(amount)
	rotated_image_2 = im.rotate(amount,expand=True)
	#The image gets cropped as some part goes out of the window when we rotate, so 'expanded=True' causes the image to zoom out
	#after being rotated so it is still completely visible

	name = filename.split(".")
	rotated_image.save(name[0]+"_rotated."+name[1])
	rotated_image_2.save(name[0]+"_rotated_expanded."+name[1])

elif oper==6:
	type_flip = int(input("1.Horizontal Flip\n2.Vertical Flip\n"))
	if type_flip==1:
		image_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
	else:
		image_flipped = im.transpose(Image.FLIP_TOP_BOTTOM)

	name = filename.split('.')
	image_flipped.save(name[0]+"_flipped."+name[1])