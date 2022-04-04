from utils.io_utils import load_image, save_image
from utils.image_utils import joined_image_gradients
from config.ps4_constants import img_storage

# 1-a
trans_a = load_image(img_storage.trans_a)
save_image(joined_image_gradients(trans_a), img_storage.ps_1_a_1)

sim_a = load_image(img_storage.sim_a)
save_image(joined_image_gradients(sim_a), img_storage.ps_1_a_2)
