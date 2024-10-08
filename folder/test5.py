
from collections import defaultdict
import math
import pprint
import unittest
import argparse

class Product(object):
    def __init__(self, type_, weight):
        self.type = type_
        self.weight = weight

    def __hash__(self):
        return hash((self.type, self.weight))

    def __eq__(self, other):
        return (self.type, self.weight) == (other.type, other.weight)

class Drone(object):
    def __init__(self, _id, x, y, capacity):
        self.id = _id
        self.x = x
        self.y = y
        self.capacity = capacity
        self.products = defaultdict(int)

    def add_product(self, product, amount):
        new_weight = self.calculate_weight() + product.weight
        if(new_weight <= self.capacity):
            self.products[product] += amount
            return True
        else:
            return False

    def remove_product(self, product, amount):
        self.products[product] -= amount

    def calculate_weight(self):
        total = 0
        for key in self.products.keys():
            total += self.products[key] * key.weight
        return total

class Warehouse(object):
    def __init__(self, _id, x, y, products):
        self.id = _id
        self.x = x
        self.y = y
        self.products = products

    def add_product(self, product, amount):
        self.products[product] += amount

    def remove_product(self, product, amount):
        self.products[product] -= amount

    def get_product_amount(self, product):
        return self.products[product]

    def calculate_weight(self):
        total = 0
        for key in self.products.keys():
            total += self.products[key]
        return total

    def __hash__(self):
        return hash((self.x, self.y, frozenset(self.products.items())))

class Order(object):
    def __init__(self, _id, x, y, products):
        self.id = _id
        self.products = products  # dictionary
        self.x = x
        self.y = y

class Simulation():
    def __init__(self, drones=[], warehouses=[], orders=[]):
        self.drones = drones
        self.warehouses = warehouses
        self.orders = orders
        self.greatest_x = 0
        self.greatest_y = 0
        for warehouse in self.warehouses:
            if(warehouse.x > self.greatest_x):
                self.greatest_x = warehouse.x
            if(warehouse.y > self.greatest_y):
                self.greatest_y = warehouse.y
    
    def tick(self):
        pass

    def load_products_from_warehouse_to_drone(self, warehouse, drone, product, amount):
        drone.add_product(product, amount)
        warehouse.remove_product(product, amount)

    def unload_products_from_drone_to_order(self, drone, order, product, amount):
        drone.remove_product(product, amount)

    def find_closest_warehouse_for_product(self, drone, product):
        best_distance = float('inf')
        best_warehouse = None
        for warehouse in self.warehouses:
            temp_dist = self.get_turns_for_distances(drone.x, drone.y, warehouse.x, warehouse.y)
            if temp_dist < best_distance:
                best_distance = temp_dist
                best_warehouse = warehouse

        return (best_warehouse, best_distance)

    def get_turns_for_distances(self, x1, y1, x2, y2):
        return math.ceil(math.sqrt((x2-x1)**2 + (y2-y1)**2))

    def calculate_minimum_turns(self, drone, order):
        (output, turns) = self.generate_output(drone, order)
        return turns

    def generate_output_for_drone(self, drone):
        output = []
        for order in self.orders:
            (output_for_order, turns) = self.generate_output(drone, order)
            output.extend(output_for_order)
        return output

    def generate_output(self, drone, order):
        turns = 0
        output = []

        product = list(order.products.keys())[0]
        amount = order.products[product]

        (warehouse, warehouse_turns_distance) = self.find_closest_warehouse_for_product(drone, product)
        turns += warehouse_turns_distance
        if (warehouse_turns_distance > 0):
            output.append(f"{drone.id} L {warehouse.id} {product.type} {amount}")
            drone.x = warehouse.x
            drone.y = warehouse.y

        self.load_products_from_warehouse_to_drone(warehouse, drone, product, amount)
        turns += 1

        turns_for_distance = self.get_turns_for_distances(drone.x, drone.y, order.x, order.y)
        turns += turns_for_distance

        return output, turns

def parse(filename):
    with open(filename, 'r') as f:
        return f.read().split('\n')

def extract_params(line):
    nums = line.split(' ')
    return {
        'rows': int(nums[0]),
        'cols': int(nums[1]),
        'D': int(nums[2]),
        'deadline': int(nums[3]),
        'max_load': int(nums[4])
    }

def extract_warehouse(w, warehouse, product_weights):
    xy = warehouse[0].split(' ')
    products = {}
    product_quantities = warehouse[1].split(' ')
    for t in range(len(product_quantities)):
        products[Product(t, product_weights[t])] = int(product_quantities[t])
    return Warehouse(w, int(xy[0]), int(xy[1]), products)

def extract_warehouses(num_warehouses, warehouses, product_weights):
    warehouses = warehouses[0:int(num_warehouses)*2:2]
    warehouse_objects = []
    for w in range(0, len(warehouses), 2):
        warehouse_objects.append(extract_warehouse(w, [warehouses[w], warehouses[w+1]], product_weights))
    return warehouse_objects

def extract_product_weights(num_product_types, product_weights):
    products = {}
    product_weights = product_weights.split(' ')
    for i in range(int(num_product_types)):
        products[i] = int(product_weights[i])
    return products

def extract_order(order_data):
    products = defaultdict(int)
    for product in order_data[2].split():
        products[int(product)] += 1
    return Order(0, int(order_data[0].split(' ')[0]), int(order_data[1].split(' ')[1]), products)

def extract_orders(num_orders, orders):
    order_objects = []
    for i in range(int(num_orders)):
        order_objects.append(extract_order([orders[i], orders[i+1], orders[i+2]]))
    return order_objects


def main():
    parser = argparse.ArgumentParser(description='Process some data.')
    parser.add_argument('filename', type=str, nargs='?', default='easy_day_at_the_office.in',
                        help='The name of the input file (default: easy_day_at_the_office.in)')
    args = parser.parse_args()

    filename = args.filename

    print('hello world')

    try:
        data = parse(filename)
        params = extract_params(data[0])
        product_weights = extract_product_weights(data[1], data[2])

        warehouses = extract_warehouses(data[3], data[4:4 + 2 * int(data[3])], product_weights)
        print(warehouses)

        orders = extract_orders(data[8], data[9:9 + 3 * int(data[8])])

        print('l')

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred while processing the file: {e}")
        exit(1)

if __name__ == "__main__":
    main()
    unittest.main()
    
class TestDrone(unittest.TestCase):
    def test_empty_drone_has_0_weight(self):
        drone = Drone(0,0,0,0)
        self.assertEqual(0, drone.calculate_weight())

    def test_drone_has_weight_one_product(self):
        drone = Drone(0,0,0,1)
        drone.add_product(Product(0, 1),1)
        self.assertEqual(1, drone.calculate_weight())

    def test_drone_has_weight_two_products(self):
        drone = Drone(0,0,0,2)
        self.assertEqual(True,drone.add_product(Product(0, 1), 1))
        self.assertEqual(True,drone.add_product(Product(0, 1), 1))
        self.assertEqual(2, drone.calculate_weight())

    def test_drone_can_calculate_weight_of_differently_sized_products(self):
        drone = Drone(0,0,0,10)
        drone.add_product(Product(0, 4), 1)
        drone.add_product(Product(0, 5), 1)
        self.assertEqual(9, drone.calculate_weight())

    def test_drone_loses_weight(self):
        drone = Drone(0,0,0,1)
        drone.add_product(Product(0, 1), 2)
        drone.remove_product(Product(0, 1), 1)
        self.assertEqual(1, drone.calculate_weight())

    def test_drone_does_not_add_product_when_full(self):
        drone = Drone(0,0,0,5)
        drone.add_product(Product(0, 5), 1)
        self.assertEqual(False, drone.add_product(Product(0, 1), 1))
        self.assertEqual(5, drone.calculate_weight())

class TestWarehouse(unittest.TestCase):
    def test_empty_warehouse_has_0_weight(self):
        warehouse = Warehouse(0, 0,0,defaultdict(int))
        self.assertEqual(0, warehouse.calculate_weight())

    def test_warehouse_has_weight_one_product(self):
        warehouse = Warehouse(0, 0,0,defaultdict(int))
        warehouse.add_product(Product(0, 10),1)
        self.assertEqual(1, warehouse.calculate_weight())

    def test_warehouse_has_weight_two_products(self):
        warehouse = Warehouse(0, 0,0,defaultdict(int))
        warehouse.add_product(Product(0, 10),1)
        warehouse.add_product(Product(0, 10),1)
        self.assertEqual(2, warehouse.calculate_weight())

    def test_warehouse_loses_weight(self):
        warehouse = Warehouse(0, 0,0,defaultdict(int))
        warehouse.add_product(Product(0, 10),2)
        warehouse.remove_product(Product(0, 10),1)
        self.assertEqual(1, warehouse.calculate_weight())

class TestOrder(unittest.TestCase):
    def test_construct_one_product(self):
        products = defaultdict(int)
        products[1] = 1
        order = Order(0, 1, 1, products)
        self.assertEqual(1, products[1])

class TestAll(unittest.TestCase):
    def test_first(self):
        self.assertEqual('hi', 'hi')