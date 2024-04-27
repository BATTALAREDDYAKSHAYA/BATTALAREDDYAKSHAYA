% Define parameters
frequencies = [100, 200, 300];  % Frequencies in Hz
amplitudes = [1, 0.5, 0.3];      % Amplitudes
duration = 1;                    % Duration in seconds
sampling_rate = 44100;           % Sampling rate in Hz

% Generate time array
t = linspace(0, duration, sampling_rate * duration);

% Generate sine wave
signal = zeros(1, length(t));
for i = 1:length(frequencies)
    signal = signal + amplitudes(i) * sin(2 * pi * frequencies(i) * t);
end

% Plot the waveform
plot(t, signal);
xlabel('Time [s]');
ylabel('Amplitude');
title('Generated Sine Wave');