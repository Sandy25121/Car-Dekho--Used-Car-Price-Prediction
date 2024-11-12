import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('Car_prediction_Random_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define OEM and model mappings (same as your current mappings)
oem_to_models = {
    'Maruti': [
        'Maruti Celerio', 'Maruti Swift', 'Maruti Wagon R', 'Maruti Baleno', 'Maruti Ciaz',
        'Maruti Ertiga', 'Maruti S-Presso', 'Maruti XL6', 'Maruti Alto', 'Maruti Ritz',
        'Maruti Alto 800', 'Maruti Vitara Brezza', 'Maruti A-Star', 'Maruti Esteem',
        'Maruti Zen Estilo', 'Maruti Eeco', 'Maruti Gypsy', 'Maruti FRONX', 'Maruti Jimny',
        'Maruti Versa', 'Maruti Omni', 'Maruti 800', 'Maruti Alto K10', 'Maruti Celerio X',
        'Maruti Swift Dzire', 'Maruti Swift Dzire Tour', 'Maruti Wagon R Stingray', 'Maruti Ertiga Tour',
        'Maruti Grand Vitara', 'Maruti Brezza', 'Maruti SX4', 'Maruti Zen', 'Maruti Baleno RS'
    ],
    'Ford': [
        'Ford Ecosport', 'Ford Figo', 'Ford Endeavour', 'Ford Aspire', 'Ford Freestyle', 'Ford Fiesta',
        'Ford Fiesta Classic', 'Ford Ikon'
    ],
    'Hyundai': [
        'Hyundai Xcent', 'Hyundai Venue', 'Hyundai Grand i10', 'Hyundai Creta', 'Hyundai Santro', 
        'Hyundai i20', 'Hyundai EON', 'Hyundai Verna', 'Hyundai Accent', 'Hyundai Tucson', 
        'Hyundai Getz', 'Hyundai Elantra', 'Hyundai Alcazar', 'Hyundai Santro Xing', 
        'Hyundai Sonata', 'Hyundai i10', 'Hyundai i20 Active', 'Hyundai Grand i10 Nios', 
        'Hyundai i20 N Line', 'Hyundai Kona', 'Hyundai Xcent Prime', 'Hyundai Aura'
    ],
    'Tata': [
        'Tata Tiago', 'Tata Nexon', 'Tata Safari', 'Tata Harrier', 'Tata Tigor', 
        'Tata Nano', 'Tata Sumo', 'Tata Indica', 'Tata Manza', 'Tata Zest', 
        'Tata Bolt', 'Tata Aria', 'Tata Hexa', 'Tata Indigo', 'Tata Punch', 
        'Tata Altroz', 'Tata New Safari', 'Tata Nexon EV', 'Tata Nexon EV Prime', 
        'Tata Nexon EV Max', 'Tata Sumo Victa', 'Tata Safari Storme', 'Tata Yodha Pickup', 
        'Tata Indigo Marina', 'Tata Tigor EV', 'Tata Indica V2'
    ],
    'Mercedes-Benz': [
        'Mercedes-Benz GLA', 'Mercedes-Benz S-Class', 'Mercedes-Benz E-Class', 
        'Mercedes-Benz C-Class', 'Mercedes-Benz GL-Class', 'Mercedes-Benz A-Class Limousine', 
        'Mercedes-Benz GLC', 'Mercedes-Benz B Class', 'Mercedes-Benz GLS', 'Mercedes-Benz A Class', 
        'Mercedes-Benz CLA', 'Mercedes-Benz AMG GT', 'Mercedes-Benz M-Class', 'Mercedes-Benz GLE', 
        'Mercedes-Benz SLC', 'Mercedes-Benz CLS-Class', 'Mercedes-Benz GLS', 'Mercedes-Benz GLC Coupe',
        'Mercedes-Benz GLA Class', 'Mercedes-Benz AMG GLA 35', 'Mercedes-Benz AMG A 35', 
        'Mercedes-Benz EQC', 'Mercedes-Benz AMG G 63', 'Mercedes-Benz AMG GLC 43'
    ],
    'BMW': [
        'BMW 3 Series', 'BMW 5 Series', 'BMW 7 Series', 'BMW X1', 'BMW X3', 'BMW X5',
        'BMW X6', 'BMW X7', 'BMW 2 Series', 'BMW 6 Series', 'BMW 3 Series GT', 'BMW 3 Series Gran Limousine',
        'BMW X4'
    ],
    'Audi': [
        'Audi A4', 'Audi A6', 'Audi A3', 'Audi Q5', 'Audi Q7', 'Audi Q3', 'Audi Q2',
        'Audi A8', 'Audi S5 Sportback', 'Audi Q3 Sportback', 'Audi A3 cabriolet'
    ],
    'Toyota': [
        'Toyota Fortuner', 'Toyota Innova', 'Toyota Yaris', 'Toyota Corolla', 'Toyota Glanza',
        'Toyota Urban cruiser', 'Toyota Innova Crysta', 'Toyota Land Cruiser 300', 
        'Toyota Camry', 'Toyota Etios', 'Toyota Corolla Altis', 'Toyota Hyryder',
        'Toyota Etios Cross', 'Toyota Etios Liva'
    ],
    'Honda': [
        'Honda City', 'Honda Civic', 'Honda BR-V', 'Honda WR-V', 'Honda Amaze', 'Honda Jazz', 
        'Honda CR-V', 'Honda Accord', 'Honda Brio', 'Honda Mobilio'
    ],
    'Volkswagen': [
        'Volkswagen Polo', 'Volkswagen Vento', 'Volkswagen Ameo', 'Volkswagen Tiguan', 
        'Volkswagen Taigun', 'Volkswagen Jetta', 'Volkswagen Passat', 'Volkswagen CrossPolo',
        'Volkswagen T-Roc', 'Volkswagen Virtus', 'Volkswagen Tiguan Allspace'
    ],
    'Nissan': [
        'Nissan Micra', 'Nissan Sunny', 'Nissan Terrano', 'Nissan Kicks', 'Nissan Magnite',
        'Nissan Micra Active'
    ],
    'MG': [
        'MG Hector', 'MG Hector Plus', 'MG Astor', 'MG ZS EV', 'MG Gloster', 'MG Comet EV'
    ],
    'Kia': [
        'Kia Seltos', 'Kia Sonet', 'Kia Carnival', 'Kia Carens'
    ],
    'Skoda': [
        'Skoda Rapid', 'Skoda Octavia', 'Skoda Superb', 'Skoda Yeti', 'Skoda Kushaq',
        'Skoda Slavia', 'Skoda Kodiaq', 'Skoda Fabia', 'Skoda Laura'
    ],
    'Jeep': [
        'Jeep Compass', 'Jeep Wrangler', 'Jeep Meridian', 'Jeep Compass Trailhawk'
    ],
    'Mahindra': [
        'Mahindra Scorpio', 'Mahindra XUV500', 'Mahindra XUV300', 'Mahindra XUV700', 
        'Mahindra Bolero', 'Mahindra Thar', 'Mahindra KUV 100', 'Mahindra Marazzo',
        'Mahindra Alturas G4', 'Mahindra Verito', 'Mahindra Quanto', 'Mahindra Bolero Neo',
        'Mahindra E Verito', 'Mahindra TUV 300', 'Mahindra TUV 300 Plus', 'Mahindra Xylo',
        'Mahindra Ssangyong Rexton', 'Mahindra Scorpio N', 'Mahindra Renault Logan',
        'Mahindra Bolero Power Plus', 'Mahindra Bolero Camper', 'Mahindra Bolero Pik Up Extra Long'
    ],
    'Fiat': [
        'Fiat Punto', 'Fiat Linea', 'Fiat Punto EVO', 'Fiat Avventura', 'Fiat Abarth Avventura',
        'Fiat Punto Pure', 'Fiat Palio', 'Fiat Grande Punto'
    ],
    'Datsun': [
        'Datsun GO', 'Datsun RediGO', 'Datsun GO Plus'
    ],
    'Chevrolet': [
        'Chevrolet Beat', 'Chevrolet Spark', 'Chevrolet Tavera', 'Chevrolet Aveo', 
        'Chevrolet Sail', 'Chevrolet Cruze', 'Chevrolet Captiva', 'Chevrolet Enjoy', 
        'Chevrolet Optra', 'Chevrolet Aveo U-VA'
    ],
    'Land Rover': [
        'Land Rover Range Rover', 'Land Rover Range Rover Sport', 'Land Rover Range Rover Evoque', 
        'Land Rover Discovery', 'Land Rover Defender', 'Land Rover Freelander 2', 
        'Land Rover Discovery Sport', 'Land Rover Range Rover Velar'
    ],
    'Volvo': [
        'Volvo XC40', 'Volvo XC60', 'Volvo XC 90', 'Volvo S60', 'Volvo S 80', 
        'Volvo V40', 'Volvo S60 Cross Country', 'Volvo S90'
    ],
    'Jaguar': [
        'Jaguar XF', 'Jaguar XE', 'Jaguar XJ', 'Jaguar F-Pace', 'Jaguar F-TYPE'
    ],
    'Mini': [
        'Mini Cooper', 'Mini 3 DOOR', 'Mini 5 DOOR', 'Mini Cooper SE', 
        'Mini Cooper Clubman', 'Mini Cooper Convertible', 'Mini Cooper Countryman'
    ],
    'Porsche': [
        'Porsche Cayenne', 'Porsche 911', 'Porsche Macan', 'Porsche Panamera'
    ],


}
# Title and Header
st.markdown("<h1 style='text-align: center; color: #FFA500;'>🚗 Car Price Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Accurate car resale value estimator!</h3>", unsafe_allow_html=True)

# Sidebar for Car Specifications
st.sidebar.title("🚗 Select Car Specifications")

# Input fields for each feature in the required order
input_values = {}

# Categorical Inputs (in the order you requested)
input_values['ft'] = st.sidebar.selectbox('Fuel Type', ['Petrol', 'Diesel', 'LPG', 'CNG', 'Electric'])
input_values['bt'] = st.sidebar.selectbox('Body Type', ['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans', 
                                                        'Pickup Trucks', 'Convertibles', 'Hybrids', 'Wagon'])
input_values['km'] = st.sidebar.slider('Mileage in KM', 0, 1000000, 50000, 1000)
input_values['transmission'] = st.sidebar.selectbox('Transmission', ['Manual', 'Automatic'])
input_values['ownerNo'] = st.sidebar.selectbox('Number of Owners', [1, 2, 3, 4, 5])
input_values['oem'] = st.sidebar.selectbox('OEM', list(oem_to_models.keys()))

# Display models based on selected OEM
selected_oem = input_values['oem']
models = oem_to_models.get(selected_oem, [])
input_values['model'] = st.sidebar.selectbox('Model', models if models else ['Select OEM first'])

input_values['Year'] = st.sidebar.selectbox('Registration Year', list(range(2002, 2024)))
input_values['Seats'] = st.sidebar.selectbox('Number of Seats', [2, 3, 4, 5])
input_values['Engine_CC'] = st.sidebar.slider('Engine CC', 600, 5000, 1000, 100)
input_values['Color'] = st.sidebar.selectbox('Color', ['White', 'Black', 'Red', 'Blue', 'Silver', 'Grey', 'Green', 'Yellow'])
input_values['Mileage'] = st.sidebar.slider('Mileage (km per liter)', 0, 140, 20)
input_values['City'] = st.sidebar.selectbox('City', ['Bangalore', 'Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Pune'])

# Encoding categorical data
ft_dict = {'Petrol': 0, 'Diesel': 1, 'LPG': 2, 'CNG': 3, 'Electric': 4}
bt_dict = {'Hatchback': 0, 'SUV': 1, 'Sedan': 2, 'MUV': 3, 'Coupe': 4, 'Minivans': 5, 
           'Pickup Trucks': 6, 'Convertibles': 7, 'Hybrids': 8, 'Wagon': 9}
transmission_dict = {'Manual': 0, 'Automatic': 1}
oem_dict = {k: idx for idx, k in enumerate(oem_to_models.keys())}
model_dict = {model: idx for idx, model in enumerate([model for models in oem_to_models.values() for model in models])}
color_dict = {'White': 0, 'Black': 1, 'Red': 2, 'Blue': 3, 'Silver': 4, 'Grey': 5, 'Green': 6, 'Yellow': 7}
city_dict = {'Bangalore': 0, 'Delhi': 1, 'Mumbai': 2, 'Chennai': 3, 'Kolkata': 4, 'Pune': 5}

# Apply encoding
input_values['ft'] = ft_dict[input_values['ft']]
input_values['bt'] = bt_dict[input_values['bt']]
input_values['transmission'] = transmission_dict[input_values['transmission']]
input_values['oem'] = oem_dict[input_values['oem']]
input_values['model'] = model_dict[input_values['model']]
input_values['Color'] = color_dict[input_values['Color']]
input_values['City'] = city_dict[input_values['City']]

# Prepare input data
input_data = [list(input_values.values())]

# Inverse encoding for display
ft_inv_dict = {v: k for k, v in ft_dict.items()}
bt_inv_dict = {v: k for k, v in bt_dict.items()}
transmission_inv_dict = {v: k for k, v in transmission_dict.items()}
oem_inv_dict = {v: k for k, v in oem_dict.items()}
model_inv_dict = {v: k for k, v in model_dict.items()}
color_inv_dict = {v: k for k, v in color_dict.items()}
city_inv_dict = {v: k for k, v in city_dict.items()}

# Prediction
predict_button = st.sidebar.button('Predict Price')
if predict_button:
    predicted_price = model.predict(input_data)[0]
    
    # Show selected information and prediction
    st.subheader("Selected Car Details:")
    st.write(f"**Fuel Type:** {ft_inv_dict[input_values['ft']]}")  # Inverse of encoded value
    st.write(f"**Body Type:** {bt_inv_dict[input_values['bt']]}")  # Inverse of encoded value
    st.write(f"**Mileage (KM):** {input_values['km']}")
    st.write(f"**Transmission:** {transmission_inv_dict[input_values['transmission']]}")  # Inverse of encoded value
    st.write(f"**Number of Owners:** {input_values['ownerNo']}")
    st.write(f"**OEM:** {oem_inv_dict[input_values['oem']]}")  # Inverse of encoded value
    st.write(f"**Model:** {model_inv_dict[input_values['model']]}")  # Inverse of encoded value
    st.write(f"**Registration Year:** {input_values['Year']}")
    st.write(f"**Seats:** {input_values['Seats']}")
    st.write(f"**Engine CC:** {input_values['Engine_CC']}")
    st.write(f"**Color:** {color_inv_dict[input_values['Color']]}")  # Inverse of encoded value
    st.write(f"**Mileage (km per liter):** {input_values['Mileage']}")
    st.write(f"**City:** {city_inv_dict[input_values['City']]}")  # Inverse of encoded value
    
    st.subheader(f"Predicted Price: ₹{predicted_price:,.2f}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Developed by Santhosh Kumar | Data Science Enthusiast 🧑‍💻</p>", unsafe_allow_html=True)
