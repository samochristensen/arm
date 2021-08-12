%% Inverse Kinematics (IK) Equations Developt from: 
%% http://motion.cs.illinois.edu/RoboticSystems/InverseKinematics.html

%% 2D Planar Manipulator
origin = [0 0];
l1 = 3; q1 = pi/2;
l2 = 3; q2 = pi;

for i=1:100
    q1 = q1 + 2*pi/100;    
    pivot1 = origin;
    effector1_x = pivot1(1) + l1 * cos(q1);
    effector1_y = pivot1(2) + l1 * sin(q1);
    effector1 = [effector1_x effector1_y];
    pivot2 = [effector1_x effector1_y];
    effector2_x = pivot2(1) + l2 * cos(q2);
    effector2_y = pivot2(2) + l2 * sin(q2);
    effector2 = [effector2_x effector2_y];

    %% Plots
    % Configuration Space
    % Task Space
    figure(1); grid on;
    ylim([-6 6]); xlim([-6 6]);

    plot(pivot1(1), pivot1(2), "o"); hold on;
    plot(pivot2(1), pivot2(2), "o"); hold on;

    plot([pivot1(1) effector1(1)], [pivot1(2) effector1(2)]); hold on;
    plot([pivot2(1) effector2(1)], [pivot2(2) effector2(2)]); hold on;
    
% the world coordinates of the end effector are given by:
    goal_x = pivot1(1) + l1 * cos(q1) + l2 * cos(q2);
    goal_y = pivot1(2) + l1 * sin(q1) + l2 * sin(q2);
    plot(goal_x, goal_y, "xr");
    
    pause(0.125);
    
end