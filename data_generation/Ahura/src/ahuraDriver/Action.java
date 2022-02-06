package ahuraDriver;

/**
 * Created by IntelliJ IDEA.
 * User: Administrator
 * Date: Mar 4, 2008
 * Time: 3:35:31 PM
 */
public class Action {

    public double accelerate;
    public double brake;
    public double clutch;
    public int gear;
    public double steering;
    public boolean restartRace;
    public int focus;

    public Action() {
    	accelerate = 0; // 0..1
        brake = 0; // 0..1
        clutch=0; // 0..1
        gear = 0; // -1..6
        steering = 0;  // -1..1
        restartRace = false;
        focus = 360;//ML Desired focus angle in degrees [-90; 90], set to 360 if no focus reading is desired!
    }
    public Action(Action a) {
    	this.accelerate = a.accelerate;
    	this.brake = a.brake;
    	this.clutch = a.clutch;
    	this.gear = a.gear;
    	this.steering = a.steering;
    	this.restartRace = false;
    	this.focus = 360;
    }
    
    public String toString () {
        //limitValues ();
        return "(accel " + accelerate  + ") " +
               "(brake " + brake  + ") " +
               "(clutch " + clutch  + ") " +
               "(gear " + gear + ") " +
               "(steer " + steering + ") " +
               "(meta " + (restartRace ? 1 : 0) 
               + ") " + "(focus " + focus //ML
               + ")";
    }

    public void limitValues () {
        accelerate = Math.max (0, Math.min (1, accelerate));
        brake = Math.max (0, Math.min (1, brake));
        clutch = Math.max(0, Math.min(1, clutch));
        steering = Math.max (-1, Math.min (1, steering));
        gear = Math.max (-1, Math.min (6, gear));
        
    }
    
    public static String getHeaderString () {
    	return "Acceleration,Braking,Clutch,Gear,Steering";
    }
    
    public String getAllValuesAsString () {
    	return accelerate + "," + brake + "," + clutch + "," + 
    			gear + "," + steering;
    }
    
}
