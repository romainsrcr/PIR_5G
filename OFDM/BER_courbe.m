clc
clear all
tab_SNR= -5:1:30;
for i= 1:length(tab_SNR)
    snr=tab_SNR(i);
    sim('OFDM_QAM_256','StopTime','1.3333e-04','ReturnWorkspaceOutputs','on');
    BER(i) = value_BER(1,1);
end
figure(1)
hold on
plot(tab_SNR,BER)
legend('ber');
title('\fontsize{13}BER en fonction du SNR');
xlabel('SNR');
ylabel('BER');
grid;
hold off

%i = position;
%vecteur = [vecteur(1:i-1) ; nouvelle_valeur ; vecteur(i:end)];
