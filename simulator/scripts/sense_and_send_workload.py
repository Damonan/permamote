
class workload:
    def __init__(self):
        self.config = {
            # name and type of workload
            'name' : 'sense_and_send',
            'type' : 'periodic',
            'period_s': 10,

            'sleep_current_A' : 1.5E-6,
            'startup_energy_J': 1.02E-3,
            'startup_period_s': 376E-3,
            'event_energy_J': 5E-4 + 8.62E-5,
            'atomic': True,
            'event_period_s': 510E-3,
            'event_period_min_s': 510E-3,
        }
