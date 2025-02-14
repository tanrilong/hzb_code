import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 加载模型
model = tf.keras.models.load_model('')

# 加载测试集
test_dir = ''

# 超参数




datagen = ImageDataGenerator(rescale=1./255)

test_generator = datagen.flow_from_directory(
    test_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    shuffle=False
)

# 评估模型
loss, accuracy = model.evaluate(test_generator)
print(f"Test Accuracy: {accuracy * 100:.2f}%")
