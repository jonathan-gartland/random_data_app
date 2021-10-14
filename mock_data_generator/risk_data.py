import random
import re


def get_minfraud_profile():
    """
    :return:
    """
    return {
        'distance': get_random_distance(),
        'ip_region': get_ip_region(),
        'ip_isp': isp_random_strings(),
        'bin_name': get_bin_name(),
        'cust_phone_in_billing_loc': get_cust_phone_in_billing_loc(),
        'anonymous_proxy': is_anonymous_proxy_value(),
        'is_trans_proxy': is_trans_proxy_value(),
        'explanation': get_quote_for_explanation_filler(),
        'free_mail': is_free_mail(),
        'ip_org': get_ip_org(),
        'ip_city': get_ip_city(),
        'phone_number': get_random_phone_number(),
        'country_match': get_country_match(),
        'country_code': get_random_country_code(),
        'high_risk_country': is_high_risk_country(),
        'score': get_random_score(),
        'risk_score': get_random_score(),
        'proxy_score': get_random_score(),
    }


# decorators?
def mostly_true():
    """mostly ~~ 99/100"""
    return (lambda: frequency([(1, False), (99, True)]))()


def sometimes_false():
    """sometimes ~~ 95/100"""
    return (lambda: frequency([(5, False), (95, True)]))()


def mostly_false():
    return not mostly_true()


def sometimes_true():
    return not sometimes_false()


def raw_network_synonyms():
    return """maze
warren
tangle
web
lattice
net
matrix
mesh 
crisscross
reticulum 
reticulation
system 
complex 
nexus 
web 
webwork           
chain
grid
net
organization
structure
system
arrangement
artery
checkerboard
circuitry
complex
convolution
crisscross
fabric
fiber
grill
grillwork
hookup
interconnections
jungle
labyrinth
maze
mesh
netting
nexus
patchwork
plexus
reticulation
reticule
screening
tessellation
tracks
wattle
weave
wiring
network"""


def isp_random_strings():
    network_synonyms = raw_network_synonyms()
    network_synonym_list = list(set(str.splitlines(network_synonyms.replace(" ", ""))))
    network_synonym_list.sort()
    return (lambda: frequency([
        (1, "{} {} {}".format(random.choice(network_synonym_list).capitalize(),
                              random.choice(network_synonym_list).capitalize(),
                              random.choice(network_synonym_list).capitalize())),
        (2, "{} {}".format(get_greek_god().capitalize(),
                           random.choice(network_synonym_list).capitalize())),
        # (3, "{}".format(random.choice(network_synonym_list).capitalize()))
    ]))()


def get_random_phone_number():
    """ generate and return a 10 digit us format phone number """

    def _random_phone_number():
        """
           http://stackoverflow.com/questions/26226801/making-random-phone-number-xxx-xxx-xxxx
        """
        n = '0000000000'
        while '9' in n[3:6] or n[3:6] == '000' or n[6] == n[7] == n[8] == n[9]:
            n = str(random.randint(10 ** 9, 10 ** 10 - 1))
        return n[:3] + '-' + n[3:6] + '-' + n[6:]

    return (lambda: _random_phone_number())()


def get_country_match():
    """

    :return:
    """
    return sometimes_true()


def is_high_risk_country():
    """

    :return:
    """
    return mostly_false()


def is_free_mail():
    """

    :return:
    """
    return sometimes_true()


def is_trans_proxy_value():
    """

    :return:
    """
    return sometimes_true()


def is_anonymous_proxy_value():
    """

    :return:
    """
    return sometimes_true()


def get_element():
    return random.choice([
        'Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon',
        'Sodium', 'Magnesium', 'Aluminum', 'Silicon', 'Phosphorus', 'Sulfur', 'Chlorine', 'Argon', 'Potassium',
        'Calcium', 'Scandium', 'Titanium', 'Vanadium', 'Chromium', 'Manganese', 'Iron', 'Cobalt', 'Nickel', 'Copper',
        'Zinc', 'Gallium', 'Germanium', 'Arsenic', 'Selenium', 'Bromine', 'Krypton', 'Rubidium', 'Strontium', 'Yttrium',
        'Zirconium', 'Niobium', 'Molybdenum', 'Technetium', 'Ruthenium', 'Rhodium', 'Palladium', 'Silver', 'Cadmium',
        'Indium', 'Tin', 'Antimony', 'Tellurium', 'Iodine', 'Xenon', 'Cesium', 'Barium', 'Lanthanum', 'Cerium',
        'Praseodymium', 'Neodymium', 'Promethium', 'Samarium', 'Europium', 'Gadolinium', 'Terbium', 'Dysprosium',
        'Holmium', 'Erbium', 'Thulium', 'Ytterbium', 'Lutetium', 'Hafnium', 'Tantalum', 'Tungsten', 'Rhenium',
        'Osmium', 'Iridium', 'Platinum', 'Gold', 'Mercury', 'Thallium', 'Lead', 'Bismuth', 'Polonium', 'Astatine',
        'Radon', 'Francium', 'Radium', 'Actinium', 'Thorium', 'Protactinium', 'Uranium', 'Neptunium', 'Plutonium',
        'Americium', 'Curium', 'Berkelium', 'Californium', 'Einsteinium', 'Fermium', 'Mendelevium', 'Nobelium',
        'Lawrencium', 'Rutherfordium', 'Dubnium', 'Seaborgium', 'Bohrium', 'Hassium', 'Meitnerium', 'Darmstadtium',
        'Roentgenium', 'Copernicium', 'Nihonium', 'Flerovium', 'Moscovium', 'Livermorium', 'Tennessine', 'Oganesson'
    ])


def get_greek_god():
    return random.choice([
        "Hyperion", "Iapetus", "Coeus", "Crius", "Cronus", "Mnemosyne",
        "Oceanus", "Phoebe", "Rhea", "Tethys", "Theia", "Themis", "Asteria",
        "Astraeus", "Atlas", "Aura", "Dione", "Eos", "Epimetheus", "Eurybia",
        "Eurynome", "Helios", "Clymene", "Lelantos", "Leto", "Menoetius",
        "Metis", "Ophion", "Pallas", "Perses", "Prometheus", "Selene",
        "Styx", "Hyperion", "Iapetus", "Coeus", "Crius", "Cronus", "Mnemosyne",
        "Oceanus", "Phoebe", "Rhea", "Tethys", "Theia", "Themis", "Thetis",
        "Arethusa", "Galene", "Psamathe", "Karkinos", "Ladon", "Leucothea",
        "Bythos", "Aphros", "Aegaeon", "Achelous", "Amphitrite",
        "Benthesikyme", "Brizo", "Ceto", "Charybdis", "Cymopoleia", "Delphin",
        "Eidothea", "Glaucus", "Stheno", "Euryale", "Medusa", "Deino", "Enyo",
        "Pemphredo", "Aello", "Ocypete", "Podarge", "Celaeno", "Nicothoe",
        "Hippocampi", "Hydros", "Nereus", "Nerites", "Oceanus", "Palaemon",
        "Poseidon", "Phorcys", "Pontos", "Proteus", "Scylla", "Aglaope",
        "Himerope", "Leucosia", "Ligeia", "Molpe", "Parthenope", "Peisinoe",
        "Raidne", "Teles", "Thelchtereia", "Thelxiope", "Actaeus", "Argyron",
        "Atabyrius", "Chalcon", "Chryson", "Damon", "Damnameneus", "Dexithea",
        "Lycos", "Lysagora", "Makelo", "Megalesius", "Mylas", "Nikon",
        "Ormenos", "Simon", "Skelmis", "Tethys", "Thalassa", "Thaumas",
        "Thoosa", "Triteia", "Triton", "Tritones", "Hades", "Zeus", "Poseidon",
        "Apollo", "Ares", "Dionysus", "Hephaestus", "Hestia", "Demeter",
        "Hera", "Artemis", "Athena", "Aphrodite", "Hermes", "Aether", "Ananke",
        "Chaos", "Chronos", "Erebos", "Eros", "Gaia", "Hemera", "Hypnos",
        "Nyx", "Uranus", "Phanes", "Pontus", "Tartarus", "Thalassa",
        "Thanatos", "Briareus", "Cottus", "Gyges", "Agrius", "Alcyoneus",
        "Otos", "Ephialtes", "Antaeus", "Argus Panoptes", "Arges", "Brontes",
        "Steropes", "Polyphemus", "Enceladus", "Geryon", "Orion", "Porphyrion",
        "Talos", "Tityos", "Typhon", "Alke", "Amechania", "Anaideia",
        "Angelia", "Apate", "Apheleia", "Aporia", "Arete", "Atë", "Bia",
        "Caerus", "Corus", "Deimos", "Dikaiosyne", "Dike", "Dolos", "Dysnomia",
        "Dyssebeia", "Eirene", "Ekecheiria", "Achos", "Ania", "Lupe", "Achlys",
        "Adephagia", "Adikia", "Aergia", "Agon", "Aidos", "Aisa",
        "Alala", "Alastor", "Aletheia", "Eleos", "Elpis", "Epiphron", "Eris",
        "Anteros", "Eros", "Hedylogos",
        "Himeros", "Pothos", "Eucleia", "Eulabeia", "Eunomia", "Eupheme",
        "Eupraxia", "Eusebeia", "Euthenia", "Gelos",
        "Geras", "Harmonia", "Hebe", "Hedone", "Heimarmene", "Homados",
        "Homonoia", "Horkos", "Horme", "Hybris",
        "Hypnos", "Ioke", "Kakia", "Kalokagathia", "Koalemos", "Kratos",
        "Kydoimos", "Lethe", "Limos", "Lyssa",
        "Mania", "Clotho", "Lachesis", "Atropos", "Momus", "Moros",
        "Nemesis", "Nike", "Nomos", "Oizys", "Epiales",
        "Morpheus", "Phantasos", "Phobetor", "Palioxis",
        "Peitharchia", "Peitho", "Penia", "Penthus", "Pepromene",
        "Pheme", "Philophrosyne", "Philotes", "Phobos", "The",
        "Phrike", "Phthonus", "Pistis", "Poine", "Polemos",
        "Ponos", "Poros", "Praxidike", "Proioxis", "Prophasis",
        "Ptocheia", "Soter", "Soteria", "Sophrosyne", "Techne",
        "Thanatos", "Thrasos", "Tyche", "Zelos"
    ])


def get_ip_org():
    return (lambda: frequency([
        (1, "{} {} {}".format(get_element(), get_dinosaur_name().capitalize(), get_element())),
        (2, "{} {}".format(get_dinosaur_name().capitalize(), get_element())),
        # (3, "{}".format(get_element()))
    ]))()


def get_random_distance():
    """
    mostly in range 1(? had zero here for some reason):20, sometimes up to 1/2 circumference of earth. 99.95%
    of the time it should get 1:20 as the set to choose from. The other 0.05% of the time it chooses from a
    range up to 12451.
    :return:
    """
    return (lambda: frequency([
        (1, "{}".format(frequency([
            (5, random.randrange(12451)), (95, random.randrange(20))
        ]))),
        (99, "{}".format(random.randrange(20))),
    ]))()


def get_random_score():
    return random.randrange(1000)


def get_random_country_code():
    """
    mostly US, sometimes others. I chose to represent the most likely countries from my limited recall
    """
    return (lambda: frequency([(1, 'NZ'), (2, 'HK'), (3, 'AU'), (4, 'UK'), (5, 'CA'), (85, 'US')]))()


def get_ip_isp():
    return isp_random_strings()


def get_ip_region():
    """
    :return: a 2 char representation of US state or territory or Canadian Provence
    """
    # do we need to weigh this to Maine? or is that just an artifact of our testing?
    return random.choice([
        'AL', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
        'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR',
        'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY',
        'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI', 'UM',
        'NL', 'PE', 'NS', 'NB', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU',
    ])


def get_cust_phone_in_billing_loc():
    """
        values: 'Yes', 'No', 'NotFound', ''
    :return:
    """
    return (lambda: frequency([(1, ''), (3, 'NotFound'), (10, 'No'), (99, 'Yes')]))()


def random_200_actual_bank_names():
    return [
        'The Security Dollar Bank', 'Great Lakes Bancorp Indiana', 'Hanna City State Bank',
        'Harris Bank Hoffman-Schaumburg', 'Pointe Bank', 'Customers Bank', 'Wadena State Bank', 'PetroBank',
        'Firstier Bank', 'Putnam County State Bank', 'Jefferson Bank and Trust Company',
        'Alpha Indian Rock Federal Savings and Loan Association', 'West Side National Bank',
        'Jefferson National Bank', 'Greer Federal Savings and Loan Association',
        'United Missouri Bank South', 'Calhoun County Bank', 'Waterville Savings and Loan Association',
        'BancFirst-Austin', 'Sherburne State Bank', 'Westminster Union Bank', 'Jonesburg State Bank',
        'Nicolet National Bank', 'Norwest Bank Bloomington', 'Norwest Bank Wisconsin Northeast',
        'Guaranty Trust Savings and Loan Association', 'Starion Financial',
        'Oconee Federal Savings and Loan Association', 'The Peoples Bank & Trust Company', 'Gibson Savings Bank',
        'The Chasewood Bank', 'American Savings Bank', 'Chelsea State Bank', 'Pontchartrain State Bank',
        'The Elkhart State Bank', 'Crestline Building and Loan Association', 'Beacon Federal', 'Ashton State Bank',
        'JLB Service Bank', 'HBank Texas', 'Southeastern Federal Savings Bank', 'Fidelity FSB',
        'Rivoli Bank & Trust', 'Norwest Bank MetroWest', 'SSB Community Bank', 'Pennsylvania Savings Association',
        'Security Federal Savings and Loan Association', 'Gilmore Bank', 'RCB Bank', 'F&M Bank-Winchester',
        'Jefferson Bank & Trust', 'M&I Tri-County Bank', 'Community Bank & Trust', 'Brenton National Bank',
        'Southeast First National Beach Bank', 'The Willard United Bank', 'Texas American Bank/Greater Southwest',
        'Marina Federal Savings and Loan Association', 'The Stephenson National Bank and Trust',
        'Norwest Bank St. Paul', 'First Option Bank', 'United Jersey Bank/Hillsborough National',
        'Bristol Federal Savings Bank', 'North Loup Valley Bank', 'Business & Professional Bank',
        'Lochaven Federal Savings and Loan Association', 'The Heights Bank', 'Mount Calvary State Bank',
        'Landmark Bank-Northwest', 'The Henry County Bank', 'Bell Federal Savings Bank',
        'Highland Federal Savings and Loan Association', 'First National Bank in Cisco',
        'The Citizens and Peoples National Bank', 'First Texas Bank', 'The Summit Trust Company',
        'First Western Bank', 'Aurora U. S. Industrial Bank', 'Firstar Bank', 'Rankin County Bank',
        'The Poca Valley Bank', 'Burt County State Bank', 'FMB-State Savings Bank', 'The Security National Bank',
        'Norwest Bank Winona', 'The Madison National Bank', 'Dearborn Bank and Trust Company',
        'Kansas National Bank and Trust Company', 'Valley Ridge Bank', 'Enfield Savings Bank',
        'North Middletown Deposit Bank', 'The Cumberland Bank', 'Partners Trust Municipal Bank',
        'The Bloomington State Bank', 'BankEast/Lakes Region', 'Savannah Bank National Association',
        'Harris Bank Round Lake', 'Gwinnett Bank & Trust Company', 'Shawmut Arlington Trust Company',
        'Peoples Security Bank', 'The Braintree Savings Bank', 'Metropolitan Capital Bank & Trust',
        'Moreauville State Bank', 'Olympic Savings Bank', 'Nevada First Thrift', 'First Federal Bank Texas',
        'American Federal Savings Bank', 'Hannibal Mutualloan and Buildinga', 'Greenhorn Valley Bank',
        'Patriot Federal Savings Bank', 'Marlin Business Bank', 'Evansville Commerce Bank', 'EurekaBank',
        'Solera National Bank', 'Commerce West Bank', 'Terrace Savings and Loan Association',
        'Acme Federal Savings and Loan Association', 'South Midland Bank',
        'State Federal Savings and Loan Association', 'Gulfshore Bank', 'Laurel Federal Savings Bank',
        'Scottrade Bank', 'Prime Security Bank', 'Montclair National Bank and Trust Company', 'Gogebic Range Bank',
        'Inter-State Savings Association', 'Old Kent Bank-Central', 'Wolfeboro National Bank',
        'Sawyer Savings Bank', 'Texas Commerce Bank-Barton Creek', 'First Federal Community Bank',
        'Liberty Bank & Trust', 'Founders Federal Savings and Loan Association', 'Central Bank Bloomfield',
        'WEX Bank', 'AYARS STATE BANK', 'United', 'Portsmouth Co-operative Bank', 'Bryan Bank & Trust',
        'Andover Bank', 'Firstar Bank Kentucky', 'Intercredit Bank', 'Firstar St. Anthony Bank',
        'Central Illinois Bank', 'Peoples Bank and Trust', 'Pioneer Savings and Loan Association',
        'Cosmopolitan Bank and Trust', 'CF Bancorp', 'The Torrance National Bank', 'Fidelity FSB',
        'The Juniata Valley Bank', 'M&I Mid-State Bank', 'First RepublicBank Henderson', 'Columbia Trust Bank',
        'The Coldwater Native Bank', 'Homestead Savings Bank', 'Hopewell Valley Community Bank',
        'Bent Tree National Bank', 'Chicago Community Bank', 'The Ramapo Bank', 'Heritage Federal Bank for Savings',
        'The North American Bank and Trust Company', 'Powell County Bank', 'Rushmore State Bank',
        'Standard Financial Corp.', 'Busey Business Bank', 'Wake Forest Federal Savings and Loan Association',
        '1ST Savings', 'Shawmut Winchester Bank', 'Saddle River Valley Bank', 'Buckley State Bank',
        'United Counties Trust Company', 'The Citizens Central Bank', 'Hull Federal Savings Bank', 'La Jolla Bank',
        'Southern Michigan Bank & Trust', 'Litchville State Bank', 'Boatmens National Bank',
        'First Northern Co-operative Bank', 'Sentry Savings and Loan Association',
        'Laconia Peoples National Bank and Trust Company', 'First Southeast Bank', 'Cambridge Trust Company',
        'Raccoon Valley State Bank', 'Tyler National Bank', 'Capital City Second National Bank',
        'Fidelity Union Bank', 'Heartland Bank', 'Broward National Bank', 'CommunityBank',
        'Sangamon Home Savings Association', 'Metro United Bank', 'Norwest Bank Wyoming Gillette',
        'Brooklyn Federal Savings Bank', 'Nutmeg Federal Savings and Loan Association', 'Valley Northern Bank',
        'Midwest Savings Bank', 'Texas Bank and Trust', 'The Globe Savings Bank', 'Navigation Bank',
        'Wu Tang Financial'
    ]


def random_bank_names():
    return [
        'Bank', 'Trust', 'Savings & Loan', 'Association', 'Federal', 'National', 'State', 'Capital',
        'First', 'American', 'Corp.', 'Credit', 'Commerce', 'Security', 'Deposit', 'Municipal',
        'Mutual', 'Thrift', 'Regional', 'Industrial', 'C.R.E.A.M', "Financial", "Ankh", ""
    ]


def bank_name_padding():
    return [
        "Big", "Giant", "Mega", "Zenith", "Apex", "Soul", "Super", "Agro", "Craic", "Kindness",
        "Crush", "Monopoly", "City", "Morpork", ""
    ]


def get_bin_name():
    """

    :return:
    """
    random_bank = (lambda: frequency([
            (1, "{} {} {}".format(random.choice(bank_name_padding()).replace(" ", ""),
                                  random.choice(random_bank_names()).replace(" ", ""),
                                  random.choice(random_bank_names()).replace(" ", ""))),
            (2, "{} {}".format(random.choice(bank_name_padding()).replace(" ", ""),
                               random.choice(random_bank_names()).replace(" ", ""))),
            (3, "{}".format(random.choice(random_bank_names())))
        ]))()

    if random.choice([0, 1]) > 0:  # just a little kicker, we have ~ 200 actual bank names we can use
        # or we just generate a random name from some strings, 50-50 which one we use here
        return_string = random.choice(random_200_actual_bank_names())
    else:
        return_string = random_bank
    return return_string.lstrip()


def descriptive_city_name_parts():
    return random.choice([
        "Windy", "Forest", "Mount", "Glen", "Port", "Shady", "Ocean", "River", "Los", "San", "Sunset", "Sunrise",
        "Moonlight", "View"
    ])


def direction():
    return random.choice(['North', 'East', 'South', 'West'])


def other_city_name_parts():
    return random.choice([
        "Megalopolis", "City", "Town", "Shire", "Glade", "Green", "Hollow", "Metropolis", "Gotham", "Coast",
        "Hill", "Woods", "Sands", "Township", "Village", "Ridge", "Land",
    ])


def geological_feature_or_process():
    return random.choice(["Glacier", "Steppe", "Butte", "Mountain", "Valley", "Fjord"])


def get_real_city_from_list():
    return get_item_from_file_list('./mock_data_seed_files/city_names.txt')


def get_ip_city():
    return (lambda: frequency([
        (1, "{} {}".format(descriptive_city_name_parts(), other_city_name_parts())),
        (2, "Los {} {}".format(descriptive_city_name_parts(), other_city_name_parts())),
        (3, "San {} {}".format(descriptive_city_name_parts(), other_city_name_parts())),
        (4, "{} {} {}".format(direction(), descriptive_city_name_parts(), other_city_name_parts())),
        (7, "{}".format(get_real_city_from_list()))
    ]))()


def get_item_from_file_list(in_path):
    with open(in_path) as f:
        names = [line.strip('\n') for line in f]
    return random.choice(names)


def get_dinosaur_name():
    return get_item_from_file_list('./mock_data_seed_files/dinosaurs.csv')


def get_real_city_name():
    return get_item_from_file_list('./mock_data_seed_files/city_names.txt')


def get_quote_for_explanation_filler():
    """
    """
    with open('./mock_data_seed_files/quotes.csv', 'r', encoding="utf-8") as f:
        quotes = [line.strip('\n') for line in f]
    lines = []
    pattern = re.compile('^\".*\"$')
    for line in quotes:
        if len(line.split(',')) > 0:
            for e in line.split(','):
                f = re.findall(pattern, e)
                if f:
                    lines.append("{}".format(str(f[0]).replace('"', '')))
    return random.choice(lines)


def frequency(pairs):
    """
    Return an element from ``pairs`` with a given frequency

    :param pairs: a list of tuples, [({frequency}, {value}), ...]
    """
    total = sum(p[0] for p in pairs)

    def pick(n):
        for (f, x) in pairs:
            if n <= f:
                return x
            n = n - f
    r = random.randrange(1, total + 1)
    return pick(r)
