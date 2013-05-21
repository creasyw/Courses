% Viterbi's algorithm for MLSE or ML decoding of (pre)coded symbols
% X: precoded/coded noisy received signal in blocks
% h: the FIR channel or the generating polynomial for the precoding case
function shat=myviterbi(X, h)
if nargin == 3 % coding case
precoding=0;
coding=1;
else
precoding=1;
coding=0;
end
% extract the parameters
h=h(:);
L=length(h);
[J N]=size(X); % J precoded/coded block length, N=number of blocks
K=J-L+1; % number of information symbols per block
S=2^(L-1); % number of states
S1=S/2;
S2=S*2;
if precoding
% noiseless outputs for all the paths in all stages
[A C B]=channel_to_alphabet(h);
D=ones(1, J); % fake frequency reponse -> programming trick only
else % coding
[A C B]=channel_to_alphabet(h, 'GF');
end

% only the survived bits are stored. Initialization here
survivor=repmat(-Inf, [S,N,J]);
% states' matric initialization
metric=repmat(Inf, [S,N]);
metric(1, :)=repmat(0, 1,N);
% a temporary variable for storing metric addition result
a=repmat(0, S,N);
% Body of Viterbi?s Algorithm
for p=1:J
% the path metrics = Euclidean distance
if p<L
noiseless= A(:,p);
elseif p>K
noiseless= B(:,p-K);
else
noiseless=C;
end
r=abs(repmat(X(p,:),S2,1)-repmat(D(p)*noiseless,1,N)).^2;
% add
a(1:2:S2-1, :) = r(1:2:S2-1, :)+metric;
a(2:2:S2, :) = r(2:2:S2,:)+metric;
% compare
metric = min( a(1:S,:), a(S+1:S2,:) ) ;
% select
survivor(:,:,p) = a(1:S,:) > a(S+1:S2,:);
end % of the VA body
% discard leading garbage bits in survivor paths
survivor(:,:,1:L-1)=[];

% backward processing to obtain the information bits
shat=repmat(0, K, N);
shat(K,:)=survivor(1,:,K);
state=2^(L-2)*survivor(1,:,K);
for k=K-1:-1:1
shat(k,:)=survivor((k-1)*S*N+S*[0:N-1]+state+1);
state=floor(state/2)+shat(k,:)*S1;
end
shat=2*shat-1;
%BER=sum(sum(s=shat))/K/N;
% Given a channel h, this function generates all the
% possible channel alphabets; works with precoding and
% coding cases
% h is the FIR channel or
% it is the generating polynomial (coeffi. in decending order) of
% the linear GF field cyclic code in the GF coding case
% if field == 'GF', then GF field symbols are generated
% A the transient state (starting outputs)
% O the steady state outputs % B the closing states outputs
function [A,O,B]=channel_to_alphabet(h, field)
L=length(h);
h=flipud(h(:));
s=0:2^(L)-1;
I=dec2bin(s)-'0';
if nargin == 1 %precoding case
I=2*I-1;
end
O=I*h;


H1=repmat(h, 1, L-1);
H2=H1;
for j=1:L-1
for i=1:L-j
H1(i,j)=0;
end
for i=L-j+1:L
H2(i,j)=0;
end
end
A=I*H1;
B=I*H2;
if nargin~= 1 % coding
O=2*mod(O, 2)-1;
% GF coding
A=2*mod(A, 2)-1;
B=2*mod(B, 2)-1;
end


