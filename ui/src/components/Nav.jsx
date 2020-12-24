import React from 'react';
import Link from 'react-router';

const Nav = () => {
    return(
        <ol>
            <li>
                <Link>Home</Link>
            </li>
            <li>
                <Link>Dance</Link>
            </li>
            <li>
                <Link>Lesson</Link>
            </li>
            <li>
                <Link>Contact</Link>
            </li>
        </ol>
    )
}