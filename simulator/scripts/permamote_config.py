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
            'active_frequency_minutes' : 1,
            'operating_voltage_V' : 3.3,
            'boost_efficiency' : 0.8,
            'frontend_efficiency' : 0.8,
            'secondary' : 'lto_battery',
            'secondary_max_percent': 80.5,
            'secondary_min_percent': 80,
        }
        self.primary_config= {
            'name' : 'primary',
            'capacity_mAh' : 480,
            'nominal_voltage_V' : 3,
            #'density_WhpL': self.chemistry_energy_density_WhpL['LiMnO2'],
            #'volume_L':   self.battery_type_to_volume_L['CR123A'],
            'leakage_percent_year' : 1,
        }
        self.secondary_lipo_config = {
            'name' : 'secondary',
            'type' : 'battery',
            'charge_discharge_eff' : 0.95,
            'capacity_mAh' : 20,
            'nominal_voltage_V' : 3.6,
            'lifetime_cycles' : 1000,
            'leakage_constant': 5E4,
        }
        self.secondary_lto_config = {
            'name' : 'secondary',
            'type' : 'battery',
            'charge_discharge_eff' : 0.95,
            'capacity_mAh' : 20,
            'nominal_voltage_V' : 2.4,
            'lifetime_cycles' : 10000,
            'leakage_constant': 5E4,
        }
        self.secondary_configs = {
            'lipo_battery' : self.secondary_lipo_config,
            'lto_battery' : self.secondary_lto_config,
        }
        self.solar_config = {
            'name' : 'solar',
            'nominal_voltage_V' : 2.5,
            'area_cm2' : 2.1*4.2,
            'efficiency' : 0.19,
        }
        self.config_list = [self.design_config, self.primary_config, self.secondary_configs[self.design_config['secondary']], self.solar_config]
