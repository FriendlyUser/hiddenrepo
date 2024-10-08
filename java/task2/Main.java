
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.List;
import java.util.Locale;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// Entities
class Product {
    private String name;
    private Double price;

    public Product() {
    }

    public Product(String name, Double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public static String staticUpperCaseName(Product p) {
        return p.getName().toUpperCase();
    }

    public String nonStaticUpperCaseName() {
        return name.toUpperCase();
    }

    public static boolean staticProductPredicate(Product p) {
        return p.getPrice() >= 100.00;
    }

    public boolean nonStaticProductPredicate() {
        return price >= 100.00;
    }

    public static void staticPriceUpdate(Product p) {
        // If price is zero or negative, set it to a default positive value (1.0)
        if (p.getPrice() <= 0) {
            p.setPrice(1.0);
        } else {
            p.setPrice(p.getPrice() * 1.1); // Increase by 10%
        }
    }

    // Non-static method to update the price and ensure it's always positive
    public void nonStaticPriceUpdate() {
        // If price is zero or negative, set it to a default positive value (1.0)
        if (price <= 0) {
            price = 1.0;
        } else {
            price = price * 1.1; // Increase by 10%
        }
    }

    @Override
    public String toString() {
        return name + ", " + String.format("%.2f", price);
    }

    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((name == null) ? 0 : name.hashCode());
        result = prime * result + ((price == null) ? 0 : price.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Product other = (Product) obj;
        if (name == null) {
            if (other.name != null)
                return false;
        } else if (!name.equals(other.name))
            return false;
        if (price == null) {
            if (other.price != null)
                return false;
        } else if (!price.equals(other.price))
            return false;
        return true;
    }
}

// Util
class UpperCaseName implements Function<Product, String> {
    @Override
    public String apply(Product p) {
        return p.getName().toUpperCase();
    }
}

class ProductPredicate implements Predicate<Product> {
    @Override
    public boolean test(Product p) {
        return p.getPrice() >= 100;
    }
}

class PriceUpdate implements Consumer<Product> {
    @Override
    public void accept(Product p) {
        p.setPrice(p.getPrice() * 1.1);
    }
}

// Services
class ProductService {
    public double filterSum(List<Product> list, Predicate<Product> criteria) {
        double sum = 0;
        for (Product p : list) {
            if (criteria.test(p)) {
                sum += p.getPrice();
            }
        }
        return sum;
    }
}

// Application
public class Main {
    public static void main(String[] args) {
        // Application 1: Function
        Locale.setDefault(Locale.US);
        List<Product> list1 = new ArrayList<>();
        list1.add(new Product("Tv", 900.00));
        list1.add(new Product("Mouse", 50.00));
        list1.add(new Product("Tablet", 350.50));
        list1.add(new Product("HD Case", 80.90));
        List<String> names = list1.stream().map(new UpperCaseName()).collect(Collectors.toList());
        names.forEach(System.out::println);

        // Application 2: Stream
        List<Integer> list2 = Arrays.asList(3, 4, 5, 10, 7);
        Stream<Integer> st1 = list2.stream().map(x -> x * 10);
        System.out.println(Arrays.toString(st1.toArray()));
        Stream<String> st2 = Stream.of("Maria", "Alex", "Bob");
        System.out.println(Arrays.toString(st2.toArray()));
        Stream<Integer> st3 = Stream.iterate(0, x -> x + 2);
        System.out.println(Arrays.toString(st3.limit(10).toArray()));
        Stream<Long> st4 = Stream.iterate(new long[]{0L, 1L}, p -> new long[]{p[1], p[0] + p[1]}).map(p -> p[0]);
        System.out.println(Arrays.toString(st4.limit(10).toArray()));

        // Application 3: Comparator
        List<Product> list3 = new ArrayList<>();
        list3.add(new Product("TV", 900.00));
        list3.add(new Product("Notebook", 1200.00));
        list3.add(new Product("Tablet", 450.00));
        list3.sort(Comparator.comparing((Product p) -> p.getName().toUpperCase()));
        list3.forEach(System.out::println);


        // Application 4: Consumer
        List<Product> list4 = new ArrayList<>();
        list4.add(new Product("Tv", 900.00));
        list4.add(new Product("Mouse", 50.00));
        list4.add(new Product("Tablet", 350.50));
        list4.add(new Product("HD Case", 80.90));
        double factor = 1.1;
        list4.forEach(p -> p.setPrice(p.getPrice() * factor));
        list4.forEach(System.out::println);

        // Application 5: Predicate
        List<Product> list5 = new ArrayList<>();
        list5.add(new Product("Tv", 900.00));
        list5.add(new Product("Mouse", 50.00));
        list5.add(new Product("Tablet", 350.50));
        list5.add(new Product("HD Case", 80.90));
        double min = 100.00;
        list5.removeIf(p -> p.getPrice() >= min);
        list5.forEach(System.out::println);

        // Application 6: Function that receives function
        List<Product> list6 = new ArrayList<>();
        list6.add(new Product("TV", 900.00));
        list6.add(new Product("Mouse", 50.00));
        list6.add(new Product("Tablet", 350.50));
        list6.add(new Product("HD Case", 80.90));
        ProductService ps = new ProductService();
        double sum = ps.filterSum(list6, p -> p.getName().charAt(0) == 'T');
        System.out.println("Sum = " + String.format("%.2f", sum));

        // Application 7: Pipeline
        List<Integer> list7 = Arrays.asList(3, 4, 5, 10, 7);
        Stream<Integer> stream1 = list7.stream().map(x -> x * 10);
        System.out.println(Arrays.toString(stream1.toArray()));
        int sum7 = list7.stream().reduce(0, Integer::sum);
        System.out.println("Sum = " + sum7);
        List<Integer> newList = list7.stream()
                .filter(x -> x % 2 == 0)
                .map(x -> x * 10)
                .collect(Collectors.toList());
        System.out.println(Arrays.toString(newList.toArray()));

        // Application 8: Reference Transparency
        List<Product> list8 = new ArrayList<>();
        list8.add(new Product("TV", 900.00));
        list8.add(new Product("Notebook", 1200.00));
        list8.add(new Product("Tablet", 450.00));
        list8.sort(Main::compareProducts);
        list8.forEach(System.out::println);


        // Application 9 negative numbers
        Product negativePriceProduct = new Product("Faulty Product", -100.00);
        System.out.println("Application 9: Comparator with negative price");
        negativePriceProduct.nonStaticPriceUpdate();
        System.out.println(negativePriceProduct.getPrice());
    }
    
    public static int compareProducts(Product p1, Product p2) {
        return p1.getPrice().compareTo(p2.getPrice());
    }
}

