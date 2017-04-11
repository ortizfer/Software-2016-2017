using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Camera_c : MonoBehaviour {

    public GameObject player;

    private Vector3 offset;
    public float moveSpeed = 10f;
    public float turnSpeed = 40f;

    void Start()
    {
        offset = transform.position - player.transform.position;
        this.transform.position = new Vector3(0.08f, 2.5f, -5.4f);
    }


    void LateUpdate()
    {
        /**
                float x = player.transform.position.x;
                float y = player.transform.position.y;
                float z = player.transform.position.z;

                float b = 2 * offset.magnitude * Mathf.Sin(player.transform.rotation.y / 2);

                x = b*Mathf.Sin(player.transform.rotation.y/2);
                z = b*Mathf.Cos(player.transform.rotation.y/2);
                
                transform.position = new Vector3(player.transform.position.x + x, y, player.transform.position.z + z) + offset;

                transform.rotation = player.transform.rotation;
            **/

        

        if (Input.GetKey(KeyCode.W))// Forward
            transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.A)) // Backward
            transform.Translate(-Vector3.forward * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.E)) //  move to left
            transform.Translate(Vector3.left * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.R)) //  move to rigth
            transform.Translate(Vector3.right * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.S)) // rotate left
            transform.Rotate(Vector3.up, -turnSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.D)) // rotate rigth
            transform.Rotate(Vector3.up, turnSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.Z)) // up
            transform.Translate(Vector3.up * moveSpeed * Time.deltaTime, Space.World);

        if (Input.GetKey(KeyCode.X)) // down
            transform.Translate(Vector3.down * moveSpeed * Time.deltaTime, Space.World);

    }
}
