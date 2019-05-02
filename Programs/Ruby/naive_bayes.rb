# Load csv data from text
require 'csv'

# Load iris data stored in CSV format
def load_iris_csv()
    csv_data = CSV.read("../../../data/iris.data", headers: true)
    return csv_data
end


data = load_iris_csv()
# Native Bayes algorithm (in progress)
# data: CSV format data.
# class_col: columns representing the data.

# Separate data into 
def generate_train_data(data, train_rate = 0.3)
    data = data.to_a
    header = data[0]
    data = data[1..data.length]
    puts data
    data_len= data.length
    train_arr = Array.new((data_len*train_rate).floor) { rand(0...(data_len*train_rate).floor) }
    test_arr = Array.new(data_len - (data_len*train_rate).floor) { rand((data_len*train_rate).floor..data_len) }
    puts train_arr.length
    puts test_arr.length
    print train_arr
    train_data = train_arr.each {|i| data[i]}
    print test_arr
    test_data = test_arr.each {|i| data[i]}
    return [header, train_data, test_data]
end

header, train_data, test_data = generate_train_data(data)

def naive_bayes(data, class_col)
    
    # Firstly, caluculate the class probability
    class_data = data[class_col]
    class_total = data[class_col].length.to_f
    class_prob = Hash.new(0)
    class_data.each { |class_data| class_prob[class_data] += 1 }
    class_data = data[class_col].uniq
    class_data.each { |class_data| class_prob[class_data] = class_prob[class_data] / class_total}
    # Extact the classes

    return [data, class_data, class_prob]

    

    # Set the key to the values
    # keys_towards_values = {}
    # values_toward_class = {}
    # column_names = data

    # Count the number of the 

end

