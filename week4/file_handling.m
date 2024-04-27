% Define data
data = [1, 2, 3; 4, 5, 6; 7, 8, 9];

% Define file name
filename = 'example.txt';

% Open the file for writing
fileID = fopen(filename, 'w');

% Write data to the file
fprintf(fileID, '%d %d %d\n', data');

% Close the file
fclose(fileID);

% Open the file for reading
fileID = fopen(filename, 'r');

% Read data from the file
read_data = fscanf(fileID, '%d', [3, 3]);

% Close the file
fclose(fileID);

% Display the read data
disp('Data read from file:');
disp(read_data);