import pylab
import pydicom
filename = 'Brain2.dcm'
ds = pydicom.dcmread(filename)
ds.dir()  # 查看病人所有信息字典keys
# print(ds.PatientName)  # 查看病人名字
print(ds) # 查看病人所有信息字典， 如果出现某key对应值编码错误，先暂时跳过该key
# how to make a fast program



#test again


#test again and again

