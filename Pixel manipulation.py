#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    width, height = img.size
    
    img = img.convert("RGB")

    encrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = img.getpixel((x, y))

            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

            encrypted_pixels.append((r, g, b))

    encrypted_img = Image.new("RGB", (width, height))
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully!")

def decrypt_image(encrypted_image_path, key):
    encrypted_img = Image.open(encrypted_image_path)
    width, height = encrypted_img.size

    decrypted_pixels = []
    for y in range(height):
        for x in range(width):
            r, g, b = encrypted_img.getpixel((x, y))

            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

            decrypted_pixels.append((r, g, b))

    decrypted_img = Image.new("RGB", (width, height))
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully!")

encrypt_image("example_image.png", key=50)

decrypt_image("encrypted_image.png", key=50)


# In[ ]:




