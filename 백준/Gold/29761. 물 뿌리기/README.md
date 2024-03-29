# [Gold I] 물 뿌리기 - 29761 

[문제 링크](https://www.acmicpc.net/problem/29761) 

### 성능 요약

메모리: 33648 KB, 시간: 1136 ms

### 분류

너비 우선 탐색, 자료 구조, 그래프 이론, 그래프 탐색, 우선순위 큐, 정렬

### 문제 설명

<p>대학원생인 당신은 현재 $N \times N$의 격자 부지에서 물의 흐름에 관해 연구하고 있다. 당신의 목표는 <strong>높이가 주어진</strong> $N^2$개의 격자 칸 중 얼마나 많은 칸에 물이 닿는지를 알아내는 것이다. 수년간의 연구 끝에, 당신은 물이 다음과 같은 규칙에 따라 확산한다는 것을 알아냈다.</p>

<ul>
	<li>각 격자 칸에서, 물의 상태는 $0,1,2,\cdots,X$의 $(X+1)$개의 정수 중 하나로 표현할 수 있다. $0$은 물이 없는 상태이며, $1,\cdots,X$는 물이 있는 상태이다.</li>
	<li>처음 물을 뿌린 칸에서 물의 상태는 $X$이다.</li>
	<li>어떠한 칸 $(x,y)$에서 인접한 칸으로 물이 확산할 때, $(x,y)$에서의 물의 상태는 영향을 받지 않는다.</li>
	<li><strong>$1$보다 큰 정수 $l$에 대하여</strong>, 물의 상태가 $l$인 칸에서 물은 다음과 같은 규칙에 따라 확산한다.
	<ul>
		<li>인접한 칸 중 현재 칸과 높이가 같은 모든 칸으로 매초 물이 확산한다. 확산한 물의 상태는 $(l-1)$이다. 단, 물의 상태가 $(l-1)$ 이상인 칸으로는 물이 확산하지 않는다.</li>
		<li>인접한 칸 중 현재 칸보다 높이가 낮은 모든 칸으로 매초 물이 확산한다. 확산한 물의 상태는 $X$이다.</li>
		<li>임의의 한 칸에서 물이 여러 번 확산할 수 있으며, 모든 칸에서 확산은 동시에 발생한다.</li>
		<li>동시에 여러 칸에서 한 칸으로 물이 확산한다면, 해당 칸의 물의 상태는 확산한 물의 상태 중 최댓값을 갖는다.</li>
	</ul>
	</li>
	<li>칸 $(x,y)$에서 물의 상태가 $0$이고, 어떠한 칸에서도 $(x,y)$로 물이 확산하지 않는다면 $(x,y)$에서 물의 상태는 $0$이다.</li>
</ul>

<p>두 칸 $(a,b)$와 $(x,y)$가 서로 인접한다는 것은 $\vert a-x\vert+\vert b-y\vert = 1$임을 의미한다. 이때 $(i,j)$는 $i$행 $j$열을 의미한다. $N\times N$ 격자의 각 칸의 높이와 최초로 물이 뿌려진 위치가 주어질 때, 물이 더이상 확산하지 않을 만큼 충분히 긴 시간이 흐른 후 물이 있는 칸, 즉 물의 상태가 $1,\cdots,X$인 칸의 수를 구하시오.</p>

### 입력 

 <p>첫 번째 줄에는 네 정수 $N$, $X$, $x$, $y$가 공백으로 구분되어 주어진다. $(1\le N\le 2\,000;$ $1\le X\le 2N;$ $1\le x,y\le N)$</p>

<p>$N$은 격자의 한 변 길이, $X$는 처음 뿌려진 물의 상태, $(x,y)$는 처음으로 물이 뿌려진 위치를 의미한다.</p>

<p>두 번째 줄부터 $N$개의 줄에 격자 부지가 주어진다. 그중 $i$번째 줄에는 $N$개의 음이 아닌 정수가 공백으로 구분되어 주어진다. 이 중 $j$번째 정수 $h_{ij}$는 $(i,j)$의 높이이다. $(0\le h_{ij}\le 100\,000)$</p>

### 출력 

 <p>물이 더이상 확산하지 않을 만큼 충분히 긴 시간이 흐른 후 물이 있는 칸의 수를 첫 줄에 출력한다.</p>

