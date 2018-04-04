import math


class config:
    def __init__(self):
        self.battery_type_to_volume_L = {
            #https://en.wikipedia.org/wiki/List_of_battery_sizes
            'AA':   ((14.5 * 1/2)**2 * math.pi * 50.5) * 1E-6,
            'AAA':  ((10.5 * 1/2)**2 * math.pi * 44.5) * 1E-6,
            'CR123A': ((17 * 1/2)**2 * math.pi * 34.5) * 1E-6,
            'CR2032':  ((20 * 1/2)**2 * math.pi * 3.2) * 1E-6,
            'HTC-titanate': ((10 * 1/2)**2 * math.pi * 20) * 1E-6,
        }
        self.chemistry_energy_density_WhpL = {
            # https://en.wikipedia.org/wiki/Comparison_of_commercial_battery_types
            'Alkaline': 320,
            'LiMnO2':   510,
            # https://en.wikipedia.org/wiki/Lithium%E2%80%93titanate_battery
            'titanate': 177,
            'LiPo':     500,
            'LiIon':    475,
        }
        self.design_config = {
            'name' : 'design',
            'intermittent' : True,
            'intermittent_mode' : 'periodic', # periodic or opportunistic
            'operating_voltage_V' : 3.3,
            'boost_efficiency' : 0.8,
            'frontend_efficiency' : 0.8,
            'secondary' : 'super_cap',
            'secondary_max_percent': 80.5,
            'secondary_min_percent': 80,
        }
        self.secondary_cap = {
            'name' : 'secondary',
            'type' : 'capacitor',
            'charge_discharge_eff' : 0.80,
            'capacity_J': (1000E-6) * (3.3**2),
            'min_capacity_J': (1000E-6) * (0.4**2),
        }
        self.secondary_super_cap = {
            'name' : 'secondary',
            'type' : 'capacitor',
            'charge_discharge_eff' : 0.75,
            'capacity_J': (1000E-6 + 7.5E-3) * (3.3**2),
            'min_capacity_J': (1000E-6 + 7.5E-3) * (0.4**2),
        }
        self.secondary_configs = {
            'cap' : self.secondary_cap,
            'super_cap' : self.secondary_super_cap,
        }
        self.solar_config = {
            'name' : 'solar',
            'nominal_voltage_V' : 2.5,
            'area_cm2' : 10,
            'efficiency' : 0.19,
        }
        self.config_list = [self.design_config, self.secondary_configs[self.design_config['secondary']], self.solar_config]

