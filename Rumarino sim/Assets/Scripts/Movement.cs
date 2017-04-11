using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Movement : MonoBehaviour {

    public float moveSpeed = 10f;
    public float turnSpeed = 40f;

	void Update () {
        if (Input.GetKey(KeyCode.UpArrow))
            transform.Translate(Vector3.forward * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.DownArrow))
            transform.Translate(-Vector3.forward * moveSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.LeftArrow))
            transform.Rotate(Vector3.up, -turnSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.RightArrow))
            transform.Rotate(Vector3.up, turnSpeed * Time.deltaTime);

        if (Input.GetKey(KeyCode.Space))
            transform.Translate(Vector3.up * moveSpeed * Time.deltaTime, Space.World);

        if (Input.GetKey(KeyCode.Minus))
            transform.Translate(Vector3.down * moveSpeed * Time.deltaTime, Space.World);
    }
}
