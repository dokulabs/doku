import { Pool } from 'pg';

const pool = new Pool({
  host: '174.138.123.61',
  port: 5432,
  database: 'postgres',
  user: 'admin',
  password: 'DOKU',
  ssl: {
    rejectUnauthorized: false, // Only for development; do not use in production without proper SSL setup
  },
});

export const GET = async () => {
  // console.log({params});
  try {
    // TODO
    // use orgID to get only necessary data and necessary fields
    // breakdown each api maybe
    const result = await pool.query(`SELECT * FROM doku` );
    // const result = await pool.query(`SELECT * FROM DOKU WHERE orgid=${params.id}` );
    return new Response(JSON.stringify(result), { status: 200 })
  } catch (error) {
    console.error('Error executing query', error);
    return new Response("Failed to fetch data", { status: 500 })
  }
}
