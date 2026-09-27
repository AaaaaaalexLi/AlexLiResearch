import VPtools as vp

path_google = r'G:\Shared drives\\'

model_name = vp.tlusty.galB_path_name.format("vis", 22000, 400, "2")
model0 = vp.tlusty.read_norm(path_google + model_name)

for i in range(100):
    print(i, flush=True)
    rotated = model0.convolveRot(100, 0.5)

print("FINISHED")