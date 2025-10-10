import sys

input = sys.stdin.readline

n = int(input())
dots = [tuple(map(int, input().split())) for _ in range(n)]

