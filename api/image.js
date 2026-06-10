export default async function handler(req, res) {
  const src = req.query.src;
  if (!src) return res.status(400).json({ error: 'Missing src' });
  try {
    const r = await fetch(src, { headers: { 'Accept': 'image/*' } });
    if (!r.ok) return res.status(r.status).json({ error: 'Fetch failed' });
    const b = await r.arrayBuffer();
    res.setHeader('Content-Type', r.headers.get('content-type')||'image/png');
    res.setHeader('Cache-Control', 'public, max-age=86400');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).send(Buffer.from(b));
  } catch(e) { res.status(500).json({ error: e.message }); }
}
