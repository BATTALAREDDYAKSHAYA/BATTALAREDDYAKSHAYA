inputFile = '/home/rguktrkvalley/Pictures/Wallpapers/WhatsApp Image 2023-09-30 at 6.39.01 PM.jpeg';

imageData = imread(inputFile);
redChannel = imageData(:,:,1);
greenChannel = imageData(:,:,2);
blueChannel = imageData(:,:,3);

redOutputFile = 'red_channel.csv';
greenOutputFile = 'green_channel.csv';
blueOutputFile = 'blue_channel.csv';
csvwrite(redOutputFile, redChannel);
csvwrite(greenOutputFile, greenChannel);
csvwrite(blueOutputFile, blueChannel);

disp('Red, green, and blue channels saved to separate CSV files successfully!');