use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let testcases: u32 = input.trim().parse().unwrap();

    for case in 0..testcases {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut nums = input.split_whitespace().map(|x| x.parse::<i32>().unwrap());
        let (m, r, n) = (nums.next().unwrap(), nums.next().unwrap(), nums.next().unwrap());

        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let street_lights: Vec<i32> = input
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect();

        let mut needed = 0;
        let mut i = 0;
        let mut covered = 0;
        let mut impossible = false;

        while covered < m {
            if i < n && street_lights[i as usize] - r <= covered {
                covered = street_lights[i as usize] + r;
                i += 1;
                needed += 1;
            } else {
                impossible = true;
                covered = 9999999;
            }

            if (i + 1) < n {
                if covered > street_lights[i as usize] - r
                    && street_lights[(i + 1) as usize] - r <= covered
                {
                    i += 1;
                }
            }
        }

        if !impossible {
            println!("Case #{}: {}", case + 1, needed);
        } else {
            println!("Case #{}: IMPOSSIBLE", case + 1);
        }
    }
}
