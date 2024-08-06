import h5py
import json
from tensorflow.keras.models import model_from_json, load_model
from tensorflow.keras.utils import get_custom_objects
from tensorflow.keras import Model


# Path to your model file
model_path = r"model/my_updated_model1.h5"

# Register the Functional class
get_custom_objects().update({"Functional": Model})

# Load the model configuration from the .h5 file
with h5py.File(model_path, 'r') as f:
    model_config = f.attrs.get('model_config')
    if model_config is not None:
        model_config = json.loads(model_config)  # No need to decode

# Modify the configuration
for layer in model_config['config']['layers']:
    if layer['class_name'] == 'DepthwiseConv2D':
        layer['config'].pop('groups', None)

# Rebuild and load the model
model_json = json.dumps(model_config)
loaded_model = model_from_json(model_json)

# Save the modified model in a new format (optional)
new_model_path = r"model/implant_classifier10.keras"
loaded_model.save(new_model_path)

# Load the weights into the model
loaded_model.load_weights(model_path)

# Use the loaded model for predictions or further processing
print("Model loaded successfully")