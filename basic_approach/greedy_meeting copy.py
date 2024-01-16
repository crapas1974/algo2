def meeting_count(meeting_list):
    meeting_list_sorted = sorted(meeting_list, key=lambda x: x[1])
    
    attended_meeting = [meeting_list_sorted[0]]
    current_meeting_finish_time = meeting_list_sorted[0][1]

    for meeting in meeting_list_sorted[1:]:
        if meeting[0] > current_meeting_finish_time:
            attended_meeting.append(meeting)
            current_meeting_finish_time = meeting[1]

    return len(attended_meeting)

def meeting_selection(meeting_list, start, finish_of_before, selected, all_schedules = None, max_count = None):
    if all_schedules == None:
        all_schedules = []
    if max_count == None:
        max_count = [0]
    if start >= len(meeting_list):
        if len(selected) == max_count[0]:
            all_schedules.append(selected[:])
        elif len(selected) > max_count[0]:
            max_count[0] = len(selected)
            all_schedules.clear()
            all_schedules.append(selected[:])
        return all_schedules, max_count

    for i in range(start, len(meeting_list)):
        meeting = meeting_list[i]
        meeting_start = meeting[0]
        meeting_finish = meeting[1]
        if meeting_start > finish_of_before:
            selected.append(meeting_list[i])
            meeting_selection(meeting_list, i + 1, meeting_finish, selected, all_schedules, max_count)
            selected.pop()
    return all_schedules, max_count

def meeting_schedules(meeting_list):
    meeting_list_sorted = sorted(meeting_list, key=lambda x: x[1])
    all_schedules = None
    max_count = None
    #meeting_selection(meeting_list_sorted, 0, 0, [], all_schedules, max_count)
    all_schedules, _ = meeting_selection(meeting_list_sorted, 0, 0, [])
    return all_schedules


def activity_selection_c(activities):
    # 활동을 종료 시간에 따라 정렬
    activities.sort(key=lambda x: x[1])

    selected_activities = [activities[0]]  # 첫 번째 활동 선택
    last_finish_time = activities[0][1]

    for start, finish in activities[1:]:
        if start > last_finish_time:
            selected_activities.append((start, finish))
            last_finish_time = finish

    return selected_activities

def activity_selection_recursive(activities, start, end, selected, all_schedules, max_count = None):
    if max_count == None:
        max_count = [0]
    if start >= len(activities):
        if len(selected) == max_count[0]:
            all_schedules.append(selected[:])
        elif len(selected) > max_count[0]:
            max_count[0] = len(selected)
            all_schedules.clear()
            all_schedules.append(selected[:])
        return

    for i in range(start, len(activities)):
        if activities[i][0] > end:
            # 활동 추가
            selected.append(activities[i])
            activity_selection_recursive(activities, i + 1, activities[i][1], selected, all_schedules)
            # 활동 제거 (백트래킹)
            selected.pop()

def activity_selection(activities):
    activities.sort(key=lambda x: x[1])
    all_schedules = []
    max_count = [0]
    activity_selection_recursive(activities, 0, 0, [], all_schedules, max_count)
    print(max_count)
    return all_schedules




def main():
    tc1 = [(9, 10), (9, 9.5), (10, 10.3), (10.3, 11), (10.4, 11.3)]
    tc2 = [(9, 10.5), (10, 11.5), (11, 12.5), (12, 13.5)]
    tc3 = [(9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18)]
    tc4 = [(9, 9.5), (10, 10.5), (11, 11.5), (12, 12.5), (13, 13.5), (14, 14.5), (15, 15.5), (16, 16.5), (17, 17.5)]
    tc5 = [(11.4, 18.5), (11.2, 12.2), (15.1, 15.3), (9.3, 13.5), (9.2, 16.1), (12.2, 18.5), (17.2, 17.5), (11.3, 15.1), (9.2, 12.2), (13.1, 14.4), (14.2, 15.5), (15.1, 18.4), (9.1, 18.3), (15.2, 18.2), (16.4, 18.4), (15.0, 15.2), (9.5, 18.2), (13.3, 18.1), (17.3, 18.3), (10.5, 16.3), (11.1, 13.2), (12.3, 16.5), (9.2, 10.4), (16.3, 18.3), (16.3, 16.5), (16.2, 17.4), (14.2, 16.1), (14.3, 15.3), (15.1, 16.1), (12.0, 17.1)]
    tc6 = [(16.0, 18), (17.1, 17.4), (12.5, 15.4), (14.3, 17.5), (17.3, 17.4), (11.2, 14.0), (9.4, 17.3), (17.5, 18), (10.5, 14.2), (13.0, 14.0), (13.5, 15.2), (15.0, 17.1), (16.3, 17.0), (11.3, 17.0), (14.0, 15.3), (9.3, 11.0), (13.0, 17.1), (13.2, 14.5), (12.3, 14.4), (14.1, 15.1), (14.3, 15.4), (13.0, 13.5), (9.2, 10.5), (14.0, 15.2), (17.5, 18), (10.3, 14.4), (13.3, 13.5), (10.5, 14.2), (11.3, 15.3), (14.2, 15.2), (16.4, 18.0), (12.4, 14.0), (11.0, 15.4), (11.0, 16.2), (11.4, 14.2), (17.0, 18.0), (9.0, 17.2), (11.1, 16.1), (13.1, 16.1), (12.2, 12.5), (14.3, 18), (16.4, 17.1), (9.4, 12.2), (9.0, 12.1), (13.0, 15.3), (11.3, 12.0), (15.1, 16.3), (9.0, 14.1), (15.5, 16.2), (12.3, 17.2), (13.5, 14.0), (15.5, 17.4), (9.1, 15.1), (9.1, 14.0), (13.1, 17.4), (17.1, 17.4), (17.1, 18), (17.5, 18), (14.3, 14.5), (17.2, 18), (11.4, 12.5), (17.1, 18), (11.4, 12.1), (14.0, 18), (10.0, 17.4), (10.1, 15.1), (11.3, 13.0), (10.5, 17.3), (14.5, 15.3), (11.3, 16.4), (16.4, 18), (13.5, 16.0), (11.1, 12.0), (15.5, 17.4), (17.4, 18), (14.4, 15.3), (17.1, 18), (17.0, 18), (12.0, 14.1), (14.3, 16.0), (9.2, 12.1), (11.1, 11.4), (12.2, 18.0), (17.3, 18), (16.4, 17.2), (16.1, 17.2), (14.3, 16.2), (12.0, 13.2), (14.0, 15.0), (12.4, 13.2), (9.2, 16.1), (15.1, 17.5), (10.2, 17.0), (11.0, 15.0), (13.2, 18.0), (17.4, 18), (14.3, 18.0), (13.2, 18.0), (14.2, 17.2), (12.5, 16.5)]
    testcases = [tc1, tc2, tc3, tc4, tc5, tc6]
    for i, tc in enumerate(testcases):
        print(f"testcase {i + 1}")
        count = meeting_count(tc)
        print(f"    참석 가능한 최대 회의 횟수 : {count}")
        selected = meeting_schedules(tc)
        print(f"    참석 가능한 회의 스케줄의 갯수 : {len(selected)}")
        print(f"    참석 가능한 회의 스케줄의 목록 : {selected}")
        print()    

    print(testcases[4])
    print("--", activity_selection_c(testcases[4]))
    print("--", activity_selection_c(testcases[5]))

    print(activity_selection(testcases[4]))
if __name__ == "__main__":
    main()