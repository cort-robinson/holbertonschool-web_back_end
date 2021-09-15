/**
 * Function returns the value returned by the promise argument that resolves first.
 * @param {Promise} chinaDownload China download
 * @param {Promise} USDownload US download
 */
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
