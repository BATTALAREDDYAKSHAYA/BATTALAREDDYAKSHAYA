% Data to be written to the CSV file
data = {'Name', 'Age', 'Gender';
        'John', 25, 'Male';
        'Lisa', 30, 'Female';
        'Bob', 35, 'Male'};

% Write data to the CSV file
csvwrite('data.csv', data);

% Read data from the CSV file
data = csvread('data.csv');

disp(data);
% Data to be written to the binary file
data = [1 2 3; 4 5 6; 7 8 9];

% Write data to the binary file
% Read data from the binary file
data = load('-binary', 'data.bin');

disp(data);