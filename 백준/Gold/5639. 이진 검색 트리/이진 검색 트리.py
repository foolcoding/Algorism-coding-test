import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

preorder_node = []
while True:
    try:
        num = int(input())
        preorder_node.append(num)
    except:
        break

def postorder(start, end):
    if start >= end:
        return

    root_value = preorder_node[start]

    # 오른쪽 서브트리의 시작 지점을 찾습니다.
    # 루트보다 큰 값이 처음 나오는 지점이 오른쪽 서브트리의 시작입니다.
    right_idx = start + 1
    while right_idx < end and preorder_node[right_idx] < root_value:
        right_idx += 1

    # 왼쪽 서브트리 재귀 호출 (start + 1 부터 right_subtree_start_idx 까지)
    postorder(start + 1, right_idx)

    # 오른쪽 서브트리 재귀 호출 (right_subtree_start_idx 부터 end 까지)
    postorder(right_idx, end)

    # 루트 노드 출력 (왼쪽, 오른쪽 서브트리 처리 후)
    print(root_value)

# 전체 트리에 대해 후위 순회 시작
postorder(0, len(preorder_node))
