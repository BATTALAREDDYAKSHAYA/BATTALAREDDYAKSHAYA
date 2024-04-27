% Load audio file
file_path = 'recent:///f3f04357eadc7528597ee048662b0c3a';
[signal, sample_rate] = audioread(file_path);

% Calculate time array
duration = length(signal) / sample_rate;
time = (0:length(signal)-1) / sample_rate;

% Plot the signal
plot(time, signal)
xlabel('Time (s)')
ylabel('Amplitude')
title('Audio Signal')
grid on