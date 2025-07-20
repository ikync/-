import argparse
import yaml
from symbiot_core import QuantumVector, RitualManager


def main():
    parser = argparse.ArgumentParser(description='Symbiot 5.2 Prototype')
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to config file')
    parser.add_argument('--mode', type=str, choices=['demo', 'run'], default='demo')
    args = parser.parse_args()

    with open(args.config) as f:
        config = yaml.safe_load(f)

    qm = QuantumVector(data=np.array(config['initial_vector']))
    rm = RitualManager(config=config)

    state = qm.resonate()
    print('State after resonance:', state)

    result = rm.execute(config['default_ritual'], {'state': state})
    print('Ritual result:', result)

if __name__ == '__main__':
    main()
