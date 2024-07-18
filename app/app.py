import streamlit as st

# Título de la aplicación
st.title("Predicción de la duración de la estancia en el centro de rescate de un perro abandonado")

# Inputs de usuario
edad = st.number_input('Edad del Perro', min_value=0.0, format="%.1f")

motivo_recogida = st.selectbox('Motivo de la recogida', ['STRAY', 'OWNER SURR', 'CONFISCATE', 'OWNED', 'RETURN', 'EUTH REQ', 'FOSTER', 'DISPO REQ', 'CRUELTY'])

motivo_abandono = st.selectbox('Motivo del abandono', ['OTC', 'BITE', 'unknown', 'FIELD', 'OTC OWNED', 'FIELD OWN',
                                                      'POLICE', 'CRUELTY', 'EVICTION', 'DANGER IN', 'PAVILLION',
                                                      'NUISANCE', 'OWNER DIE'])

raza = st.selectbox('Raza', ['Shih Tzu', 'Bichon Frise', 'American Staffordshire Terrier', 'Border Terrier', 
                             'English Springer Spaniel', 'Russell Terrier (Jack Russell)', 'Pembroke Welsh Corgi',
                             'Shiba Inu', 'Cocker Spaniel', 'Miniature Pinscher', 'Collie', 'Boxer', 'Chihuahua', 
                             'Tibetan Terrier', 'Yorkshire Terrier', 'Labrador Retreiver', 'Rat Terrier', 'Pointer',
                             'Pug', 'English Cocker Spaniel', 'Treeing Walker Coonhound', 'Pekingese', 'Brussels Griffon',
                             'Japanese Chin', 'Harrier', 'German Shepherd Dog', 'Rottweiler', 'Beagle', 'Basenji',
                             'Dachshund', 'Boston Terrier', 'Chow Chow', 'Lakeland Terrier', 'Chinese Crested',
                             'Cavalier King Charles Spaniel', 'Scottish Terrier', 'Siberian Husky', 'Papillon',
                             'West Highland White Terrier (Westie)', 'Chinese Shar-Pei', 'Irish Setter', 'Maltese', 
                             'French Bulldog', 'Border Collie', 'Bulldog', 'Akita', 'Australian Cattle Dog', 
                             'Golden Retriever', 'Poodle', 'Finnish Spitz', 'Norfolk Terrier', 'Keeshond', 'Mastiff',
                             'Great Pyrenees', 'Cairn Terrier', 'Weimaraner', 'Miniature Schnauzer', 'Lhasa Apso',
                             'Catahoula Leopard Dog', 'Rhodesian Ridgeback', 'Pomeranian', 'Shetland Sheepdog',
                             'Otterhound', 'Doberman Pinscher', 'Vizsla', 'Basset Hound', 'Australian Shepherd', 
                             'American Foxhound', 'Manchester Terrier (Standard)', 'Redbone Coonhound', 'Bullmastiff',
                             'Cane Corso', 'Wire Fox Terrier', 'Anatolian Shepherd Dog', 'German Shorthaired Pointer',
                             'Norwich Terrier', 'Field Spaniel', 'Dalmatian', 'Schipperke', 'Poodle (Toy)', 
                             'Standard Schnauzer', 'Whippet', 'American Eskimo Dog', 'Italian Greyhound', 
                             'Giant Schnauzer', 'Cardigan Welsh Corgi', 'Australian Terrier', 'Airedale Terrier',
                             'Belgian Malinois', 'Black and Tan Coonhound', 'Samoyed', 'English Foxhound', 'Affenpinscher',
                             'Gordon Setter', 'Greyhound', 'Bedlington Terrier', 'Bull Terrier', 'Belgian Sheepdog',
                             'Great Dane', 'Presa Canario', 'Portuguese Water Dog', 'Welsh Terrier', 'Irish Terrier',
                             'Welsh Springer Spaniel', 'Soft Coated Wheaten Terrier', 'Skye Terrier', 'Smooth Fox Terrier',
                             'Bluetick Coonhound', 'Plott', 'Greater Swiss Mountain Dog', 'Toy Fox Terrier',
                             'Petit Basset Greiffon Vendeen (PBGV)', 'Silky Terrier', 'Tibetan Spaniel', 'Lowchen',
                             'English Setter', 'Alaskan Malamute', 'Coton de Tulear', 'Havanese', 'Flat-Coated Retreiver',
                             'Bloodhound', 'Brittany', 'Dogo Argentino', 'Dutch Shepherd', 'Treeing Tennessee Brindle',
                             'Saint Bernard', 'Treeing Cur', 'German Wirehaired Pointer', 'Grand Basset Griffon Vendeen',
                             'Clumber Spaniel', 'Wirehaired Pointing Griffon', 'Pharaoh Hound', 'Chesapeake Bay Retriever',
                             'Canaan Dog', 'Neapolitan Mastiff', 'American English Coonhound', 'Patterdale Terrier',
                             'Spinone Italiano', 'Bearded Collie', 'Bernese Mountain Dog', 'Jindo', 'Dandie Dinmont Terrier',
                             'Irish Wolfhound', 'Afghan Hound', 'Working Kelpie', 'Dogue de Bordeaux'])

raza_secundaria = st.selectbox('Raza secundaria', ['unknown', 'MIX', 'JACK RUSS TER', 'GERM SHEPHERD', 'LABRADOR RETR',
                                                   'BOXER', 'BEAGLE', 'POODLE MIN', 'BASSET HOUND', 'CHIHUAHUA SH',
                                                   'PIT BULL', 'PUG', 'BORDER COLLIE', 'DACHSHUND MIN', 'GOLDEN RETR',
                                                   'SHIH TZU', 'DALMATIAN', 'CHOW CHOW', 'SHETLD SHEEPD', 'ROTTWEILER',
                                                   'SHIBA INU', 'LHASA APSO', 'MIN PINSCHER', 'FLAT COAT RET', 'BULLDOG',
                                                   'YORKSHIRE TER', 'WELSH CORGI P', 'CAIRN TERRIER', 'BLUETICK HOUN',
                                                   'SCHNAUZER MIN', 'AM PIT BULL T', 'POODLE TOY', 'WEIMARANER', 'MALTESE',
                                                   'AMER BULLDOG', 'BULLMASTIFF', 'COLLIE ROUGH', 'CATAHOULA', 'PATTERDALE TE',
                                                   'BICHON FRISE', 'PODENGO PEQUE', 'FOX TERR SMOO', 'BELG MALINOIS', 
                                                   'DACHSHUND STD', 'DOBERMAN PINS', 'MASTIFF', 'GREYHOUND', 'RAT TERRIER',
                                                   'TIBETAN TERR', 'POODLE STND', 'RHOD RIDGEBAC', 'CHINESE SHARP', 
                                                   'COCKER SPAN', 'TREEING CUR', 'POMERANIAN', 'MANCHESTER TE', 'POINTER',
                                                   'WELSH CORGI C', 'BORDER TERRIE', 'TENN TR BRIND', 'BOSTON TERRIE',
                                                   'AUST CATTLE D', 'AUST SHEPHERD', 'AMERICAN STAF', 'DACHSHUND WH', 
                                                   'VIZSLA', 'CHIHUAHUA LH', 'TR WALKER HOU', 'BRITTANY', 'PLOTT HOUND',
                                                   'SIBERIAN HUSK', 'SCHNAUZER STA', 'PEKINGESE', 'BLOODHOUND', 'CAVALIER SPAN',
                                                   'COLLIE SMOOTH', 'PAPILLON', 'ALASK MALAMUT', 'PHAROH HOUND', 'ST BERNARD RG',
                                                   'ENG FOXHOUND', 'GREAT DANE', 'ITAL GREYHOUN', 'BLACK/TAN HOU', 'AMER FOXHOUND',
                                                   'DACHSHUND LH', 'GERM SH POINT', 'FINNISH SPITZ', 'CAROLINA DOG', 'WHIPPET',
                                                   'AKITA', 'STAFFORDSHIRE', 'BEARDED COLLI', 'SC WHEAT TERR', 'TOY FOX TERRI',
                                                   'FOX TERR WIRE', 'REDTICK HOUND', 'SILKY TERRIER', 'GORDON SETTER', 
                                                   'IRISH SETTER', 'BULL TERRIER', 'SCOT TERRIER', 'BULL TERR MIN', 'FRENCH BULLDO',
                                                   'BASENJI', 'AMER ESKIMO', 'GR SWISS MTN', 'HARRIER', 'CHINESE CREST',
                                                   'GREAT PYRENEE', 'REDBONE HOUND', 'ENG BULLDOG', 'NORFOLK TERRI'])

kennel_card_breed = st.radio('Kennel Card Breed', ['Yes', 'No'])

# Botón de predicción
if st.button('Predecir Duración de Estancia'):
    # Aquí se colocaría el código de predicción de tu modelo de machine learning
    st.write("Predicción en proceso...")

    # Simulación de un resultado de predicción