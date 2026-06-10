export default async function handler(req, res) {
  const src = req.query.src;
  if (!src) {
    return res.status(400).json({ error: 'Missing src parameter' });
  }

  try {
    const response = await fetch(src, {
      headers: { 'Accept': 'image/*' },
    });

    if (!response.ok) {
      return res.status(response.status).json({ error: 'Image fetch failed' });
    }

    const contentType = response.headers.get('content-type') || 'image/png';
    const buffer = await response.arrayBuffer();

    res.setHeader('Content-Type', contentType);
    res.setHeader('Cache-Control', 'public, max-age=86400');
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.status(200).send(Buffer.from(buffer));
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
