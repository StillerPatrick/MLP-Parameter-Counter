

def num_parameters(input_size:int, num_hidden:int, hidden_size:int, output_size:int):
    # weights input hidden
    w_inp_hidden = input_size * hidden_size

    #weights hidden layer
    w_hidden_hidden = (hidden_size ** 2)* (num_hidden-1)

    #weights 
    w_hidden_output = hidden_size * output_size

    #biases_hidden
    b_hidden = hidden_size * num_hidden

    #biases output 
    b_output = output_size

    return w_inp_hidden + w_hidden_hidden + w_hidden_output + b_hidden + b_output


if __name__ == "__main__":

    input_size = int(input("Input Size ? "))
    num_hidden = int(input("Number of Hidden Layer? "))
    hidden_size = int(input("Number of Neurons per Hidden Layer?"))
    output_size = int(input("Output Size ?"))

    number_of_parameters = num_parameters(input_size,num_hidden,hidden_size,output_size)
    print("Number of Parameters is", number_of_parameters)

    