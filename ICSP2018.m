clear all
close all
clc

%files
file = 'earlySyst-14v2.wav'; %threshold=.05, fs=3.5, delta1=300, delta2=500, early systolic, 25/25
%file = 'Normal[2].wav'; %threshold=.05, fs=3.5, delta1=300, delta2=500, normal, 9/9
%file = 'a0001.wav'; %threshold=.05, fs=3.5, delta1=300, delta2=500, normal, 71/71
%file = 'a0002.wav'; %threshold=.03, fs=3.5, delta1=300, delta2=500, holosystolic, 52/52
%file = 'a0003.wav'; %threshold=.09, fs=3.5, delta1=300, delta2=500, normal, 50/50
%file = 'a0004.wav' %threshold=.06, fs=5, delta1=400, delta2=1100, normal, 71/71
%file = 'a0005.wav'; %threshold=.12, fs=5, delta1=400, delta2=700, normal, 102/102
%file = 'a0006.wav'; %indistinguishable by eye
%file = 'a0007.wav'; %threshold=.2, fs=5, delta1=400, delta2=1100, normal
%file = 'a0008.wav'; %indistinguishable by eye
%file = 'a0009.wav'; %indistinguishable by eye
%file = 'a0010.wav'; %threshold=.04, fs=4, delta1=300, delta2=600, early systolic, 82/83
%file = 'a0011.wav'; %dramatic heart rate changes
%file = 'a0012.wav'; %threshold=.15, fs=3.5, delta1=400, delta2=700, normal, 56/56
%file = 'a0014.wav'; %indistinguishable  
%file = 'a0016.wav'; %threshold=.32, fs=3.5, delta1=400, delta2=700, diastolic, 60/64
%file = 'a0017.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, diastolic, 74/76


%file = 'b0006.wav'; %threshold=.34, fs=3.5, delta1=300, delta2=600, systolic, 19/20
%file = 'c0001.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, systolic, 
%file = 'c0003.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, early systolic
%file = 'c0007.wav'; %threshold=.3, fs=3.5, delta1=500, delta2=1100, diastolic, 68/69
%file = 'c0010.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, holosystolic
%file = 'c0011.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, normal, 210/218
%file = 'c0012.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, holosystolic
%file = 'c0013.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=700, early systolic
%file = 'c0016.wav'; %threshold=.17, fs=3.5, delta1=400, delta2=1100, normal, 63/64
%file = 'c0019.wav'; %threshold=.03, fs=3.5, delta1=400, delta2=1100, early systolic, 74/76


%load files + plot
[wave,fs]=audioread(file); 
t=0:1/fs:(length(wave)-1)/fs;  
plot(t,wave); 
hold on;
%wave = abs(wave);



%set threshold + plot
threshold = .15;
last = length(t);%max index
lasttime = t(end); %max time
plot([0, lasttime], [threshold, threshold])
sample = round(fs/3.5); %sample window

%initialize potential max value array 
potential = [];
ctr = 1; %array counter

%finds all potential max values above threshold in file
for i = 1:sample:(last-sample)
    temp = wave(i:(i+sample));
    x = find(temp == max(temp));
    actual = (wave(x(1)+i));
    index = (x(1)+i);
    if actual>threshold
        potential(ctr) = index;
        ctr = ctr + 1;
    else
    end
end

potential

%text(t(noduplicate(i-1)),wave(noduplicate(i-1)),txts)
%0 = systole; 1 = diastole
%txts = '\leftarrow s';
%txtd = '\leftarrow d';

%find and identify first 2 heart sounds
%1=s 2=d
delta1 = 400;
delta2 = 700;
if potential(2)-potential(1) > potential(3)-potential(2)
    current = 2;
    diff1 = potential(3)-potential(2);
    diff2 = potential(2)-potential(1);
    min1 = diff1-delta1
    min2 = diff2-delta1
    max1 = diff1+delta2
    max2 = diff2+delta2
else
    current = 1;
    diff1 = potential(2)-potential(1);
    diff2 = potential(3)-potential(2);
    min1 = diff1-delta1
    min2 = diff2-delta1
    max1 = diff1+delta2
    max2 = diff2+delta2
end

potential
final = [];

while length(potential) > 1
    one = potential(1);
    two = potential(2);
    two-one
    t(potential(1))
    if current == 1
        if max1 > two - one && two - one > min1
            final = [final,potential(1)];
            diff1 = two-one;
            min1 = diff1-delta1
            max1 = diff1+delta2
            current = 2
            potential(1) = [];
        else
            potential(2) = [];
        end
    elseif current == 2
        if max2 > two - one && two - one > min2
            final = [final, potential(1)];
            diff2 = two-one;
            min2 = diff2-delta1
            max2 = diff2+delta2
            current = 1
            potential(1) = [];
        else
            potential(2) = [];
        end
    end
end
noduplicate = final;

first = 1;
last = 0;
prevval = -1;
total = 0;
%0 = systole; 1 = diastole
txts = '\leftarrow s';
txtd = '\leftarrow d';
 for i = 1:length(noduplicate)
     if i == 2
         first = 0;
     end
     if i == length(noduplicate)
         last = 1;
         if prevval == 1
             text(t(noduplicate(i)),wave(noduplicate(i)),txts)
             total=total+1;
             
         else
           text(t(noduplicate(i)),wave(noduplicate(i)),txtd)
           total=total+1;
           
         end
     end
     if first==0 && last==0
        prevt = t(noduplicate(i-1));
        currentt = t(noduplicate(i));
        nextt = t(noduplicate(i+1));
        if currentt-prevt > nextt-currentt %checks if systole
           text(t(noduplicate(i)),wave(noduplicate(i)),txts)
           prevval = 0;
           total=total+1;
           
           if i == 2
               text(t(noduplicate(i-1)),wave(noduplicate(i-1)),txtd)
               total=total+1;
               
           end
        
        else %checks if diastole
           txt2 = '\leftarrow d';
           text(t(noduplicate(i)),wave(noduplicate(i)),txtd)
           total=total+1;
           
           prevval = 1;  
           if i == 2
               txt2 = '\leftarrow s';
               text(t(noduplicate(i-1)),wave(noduplicate(i-1)),txts)
               total=total+1;
               
           end
        end
     end
 end
 total