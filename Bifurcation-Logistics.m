% Logistic growth function
logistic_growth = @(r, y, K) r * y .* (1 - y / K);

% Parameters
K = 100; % Carrying capacity
r_values = linspace(0, 4, 1000); % Range of growth rates
num_iterations = 1000; % Number of iterations for each parameter value
num_transient_iterations = 500; % Number of transient iterations to discard

% Initialize the bifurcation diagram matrix
bifurcation_diagram = zeros(num_iterations - num_transient_iterations, length(r_values));

% Iterate over each growth rate
for i = 1:length(r_values)
    r = r_values(i);
    y = 0.5; % Initial condition

    % Transient iterations
    for j = 1:num_transient_iterations
        y = y + logistic_growth(r, y, K);
    end

    % Collect data for the bifurcation diagram
    for j = 1:(num_iterations - num_transient_iterations)
        y = y + logistic_growth(r, y, K);
        bifurcation_diagram(j, i) = y;
    end
end

% Plot the bifurcation diagram
figure;
plot(r_values, bifurcation_diagram, '.', 'MarkerSize', 1, 'color', 'black');
xlabel('Growth Rate(r)', 'Fontsize', 15);
ylabel('Population(N)', 'Fontsize', 15);
% xlim([0 4]); ylim([0 200]);
% title('Bifurcation Diagram for Logistic Growth Model');
