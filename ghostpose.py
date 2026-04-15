import cv2
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Default situation
situation = "STREET" 

print("Controls: 1=Park, 2=Graduation, 3=Street, q=Quit")

while True:
    success, frame = cap.read()
    if not success: break
    
    frame = cv2.flip(frame, 1) # Mirror effect
    h, w, _ = frame.shape
    center_x = int(w/2)

    # --- 1. CHANGE POSE ACC TO SITUATION ---
    key = cv2.waitKey(1) & 0xFF
    if key == ord('1'): situation = "PARK (Sitting)"
    if key == ord('2'): situation = "GRADUATION (Celebration)"
    if key == ord('3'): situation = "STREET (Standing)"

    # --- 2. DRAWING DYNAMIC GHOST LINES ---
    color = (255, 255, 255) # White
    
    if situation == "PARK (Sitting)":
        # Sitting Pose
        cv2.circle(frame, (center_x, int(h*0.4)), 35, color, 2) # Head lower
        cv2.rectangle(frame, (center_x-50, int(h*0.5)), (center_x+50, int(h*0.8)), color, 2) # Body
        cv2.putText(frame, "AI SUGGESTION: Sitting Pose for Bench", (20, 40), 1, 1.2, (0, 255, 0), 2)

    elif situation == "GRADUATION (Celebration)":
        # Graduation Pose (One hand up)
        cv2.circle(frame, (center_x, int(h*0.3)), 35, color, 2) # Head
        cv2.line(frame, (center_x, int(h*0.4)), (center_x, int(h*0.7)), color, 2) # Spine
        cv2.line(frame, (center_x, int(h*0.45)), (center_x+80, int(h*0.25)), color, 2) # Raising Degree
        cv2.putText(frame, "AI SUGGESTION: Graduation Pose", (20, 40), 1, 1.2, (0, 255, 0), 2)

    else: # Default Street Standing
        # Standard Standing Pose
        cv2.circle(frame, (center_x, 100), 40, color, 2) # Head
        cv2.line(frame, (center_x, 140), (center_x, 350), color, 2) # Body
        cv2.line(frame, (center_x-80, 220), (center_x+80, 220), color, 2) # Arms
        cv2.putText(frame, "AI SUGGESTION: Street Portrait", (20, 40), 1, 1.2, (0, 255, 0), 2)

    # Display window
    cv2.imshow('GhostPose AI - Situational Assistant', frame)
    
    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()