% Open a file in write mode
fid = fopen("text_file.txt", "w");

% Write content to the file
fprintf(fid, "Hello, this is a text file.\n");
fprintf(fid, "This file is opened in normal mode (text mode).\n");

% Close the file
fclose(fid);

% Open a file in read mode
fid = fopen("text_file.txt", "r");

% Read content from the file
content = fread(fid, "*char")';

% Display content
disp(content);

% Close the file
fclose(fid);


% Open a file in binary write mode
fid = fopen("binary_file.bin", "wb");

% Write content to the file
fwrite(fid, [1, 2, 3], "uint8");

% Close the file
fclose(fid);


% Open a file in binary read mode
fid = fopen("binary_file.bin", "rb");

% Read content from the file
content = fread(fid, "*uint8");

% Display content
disp(content);

% Close the file
fclose(fid);
