from path import Path

d = Path('nombreDeLaLocalizacionDeLosFiles')
#Replace DIRECTORY with your required directory

num_files = len(d.files())

print(num_files)

#replace directory with your desired directory
for i in d.walk():
    if i.isfile():
        if i.name.startswith('file'):
            i.remove()

num_files = len(d.files())
print(num_files)